from django.shortcuts import render

from .forms import ImageDetectionForm

from .models import ImageDetection

import cv2

import os

from django.conf import settings

from ultralytics import YOLO


# Load the YOLO model globally

model = YOLO('yolov8n.pt')


def detect_objects(request):

    if request.method == 'POST' and 'uploaded_image' in request.FILES:

        form = ImageDetectionForm(request.POST, request.FILES)

        

        if form.is_valid():

            # Save the form instance to create a record in the database

            image_detection = form.save()

            

            # Read the uploaded image

            uploaded_image_path = image_detection.uploaded_image.path

            image = cv2.imread(uploaded_image_path)

            

            # Run YOLO detection

            results = model(image)

            

            # Annotate the image (accessing the first result, as it should contain one image)

            annotated_image = results[0].plot()  # 'results[0]' contains the detection result for the image

            

            # Define the path to save the annotated image

            output_image_name = f"output_{image_detection.id}.jpg"

            output_image_path = os.path.join(settings.MEDIA_ROOT, output_image_name)

            

            # Save the annotated image

            cv2.imwrite(output_image_path, annotated_image)

            

            # Save the URL of the annotated image to the database

            image_detection.output_image = os.path.join(settings.MEDIA_URL, output_image_name)

            image_detection.save()


            # Prepare detection results to pass to the template

            detection_results = []

            for box, score, class_id in zip(results[0].boxes.xywh, results[0].boxes.conf, results[0].boxes.cls):

                detection_results.append({

                    'name': model.names[int(class_id)],

                    'confidence': round(score.item() * 100, 2)  # Convert to percentage

                })

            

            # Return the template with results

            return render(

                request,

                'home.html',

                {

                    'form': form,

                    'uploaded_image': image_detection.uploaded_image,

                    'output_image': image_detection.output_image,

                    'detection_results': detection_results

                }

            )

        else:

            # Handle form validation failure

            return render(request, 'home.html', {'form': form, 'error': 'Invalid form submission.'})


    else:

        form = ImageDetectionForm()

        return render(request, 'home.html', {'form': form})

