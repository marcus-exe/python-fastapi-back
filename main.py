from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
# from utils import my_module
import os
from datetime import datetime

# Create an instance of the FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/image")
def read_image():
    # my_module.ai_api()

    image_path = "utils/input/teste.jpeg"

    # Check if the file exists
    if not os.path.isfile(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    
    return FileResponse(image_path, media_type="image/jpeg")


@app.post("/image")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Ensure the directory exists
        os.makedirs('./utils/input', exist_ok=True)

        # Generate a timestamp-based filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_extension = file.filename.split('.')[-1]  # Get file extension
        file_path = f'./utils/input/uploaded_image_{timestamp}.{file_extension}'
        
        # Save the file with the new filename
        with open(file_path, "wb") as image_file:
            image_file.write(await file.read())
        
        # Return the uploaded image file as a response
        return FileResponse(file_path, media_type=f"image/{file_extension}", headers={"Content-Disposition": f"attachment; filename={os.path.basename(file_path)}"})
    
    except Exception as e:
        print(f"Error during file upload: {e}")  # Log the error
        return JSONResponse(status_code=400, content={"message": str(e)})
