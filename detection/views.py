from ultralytics import YOLO

from django.shortcuts import render

from .forms import ImageDetectionForm  # Import your form

from .models import ImageDetection  # Import your ImageDetection model

import cv2

import os

from django.conf import settings  # Import settings for MEDIA_ROOT and MEDIA_URL


# Load the YOLO model globally to avoid reloading it on every request

model = YOLO('yolov8n.pt')



def detect_objects(request):

    if request.method == 'POST' and 'uploaded_image' in request.FILES:

        form = ImageDetectionForm(request.POST, request.FILES)

        

        if form.is_valid():

            # Save the form instance to create a record in the database

            image_detection = form.save()

            

            # Read the uploaded image using its absolute path

            uploaded_image_path = image_detection.uploaded_image.path

            image = cv2.imread(uploaded_image_path)

            

            # Run YOLO detection on the image

            results = model(image)

            

            # Annotate the image with detection results using plot() on the first result

            annotated_image = results[0].plot()  # Use the first Results object in the list

            

            # Define the path to save the annotated image

            output_image_name = f"output_{image_detection.id}.jpg"  # Use unique names to avoid overwriting

            output_image_path = os.path.join(settings.MEDIA_ROOT, output_image_name)

            

            # Save the annotated image

            cv2.imwrite(output_image_path, annotated_image)

            

            # Update the ImageDetection instance with the output image URL

            image_detection.output_image = os.path.join(settings.MEDIA_URL, output_image_name)

            image_detection.save()

            

            # Return the response with uploaded and output image URLs

            return render(

                request,

                'home.html',

                {

                    'form': form,

                    'uploaded_image': image_detection.uploaded_image.url,  # URL for uploaded image

                    'output_image': image_detection.output_image  # URL for output image

                }

            )

        else:

            # Handle invalid form submission

            return render(

                request,

                'home.html',

                {

                    'form': form,

                    'error': 'Invalid form submission.'

                }

            )

    else:

        # Render an empty form for GET requests

        form = ImageDetectionForm()

        return render(request, 'home.html', {'form': form})

