1. Download the required materials:

- Github Repository: https://github.com/naavie/Food-101-Classification
- Pre-trained ResNet-50 model: https://drive.google.com/uc?id=1JfJD0tFnnI3iOCQTP2lwnvmV8oPmsQXy&export=download

2. After downloading the Github repository, download the pre-trained ResNet-50 model by following the link
above and place the downloaded model into the same folder where the Dockerfile is. The ResNet-50 model is
saved as the file “checkpoint.pth.tar”

- NOTE: DO NOT EXTRACT “checkpoint.pth.tar”. Simply drag it into the main repository folder within your
workspace.

    ![Alt text](model_placement_dir.png)

3. Open the repository in VSCode or your preferred code editor program: 

    ![Alt text](Open_VSCode.png)

4. Start your Docker Engine and run the following commands in Command Prompt/Terminal:

- docker build -t <"your image name"> .

    ![Alt text](dockerbuilt_example.png)

- docker run -p 5000:5000 <"your image name">

    ![Alt text](dockerrun_example.png)

    Please replace <"your image name"> with any name of your choosing and without the <> symbols. Please also
    run the docker run command in a command prompt terminal. Do not run it within an integrated code editor like
    VSCode/Vim/etc.

    After you execute the docker run command, you can open the localhost:5000 on any web browser (Google
    Chrome is recommended) and experiment with the ML-service.

    All code runs on Python 3.8 and the list of necessary modules/libraries can be found in requirements.txt file.

    All specific details on how to run and use the service can be found on the web service webpage

5. If you are using Docker Desptop, open the URL for the corresponding container, else you can go to http://localhost:5000/ on your webbrowser until you are taken to a screen that looks like this: 

    ![Alt text](webpage.png)

6. You're all set! Scroll to the Live Demonstration section and upload your image. Click Upload and the page will refresh and your Image Class prediction will be shown on the "Image Prediction" line. 
