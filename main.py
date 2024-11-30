from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from utils import my_module
import os
from datetime import datetime

# Create an instance of the FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/image")
def read_image():
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
        file_name = f'uploaded_image_{timestamp}.{file_extension}'
        file_path = f'./utils/input/{file_name}'
        
        # Save the file with the new filename
        with open(file_path, "wb") as image_file:
            image_file.write(await file.read())

        model_path = r'./utils/best.pt'
        output_dir = r'./utils/output/'

        my_module.ai_api(file_path, model_path)
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        base_path = "runs/segment/"
        last_path = get_last_alphabetical_dir(base_path)
        # complete_path = f'{base_path}{last_path}/'
        image_name_and_extension = get_single_file_name(last_path) 
        image_full_path = f'{last_path}/{image_name_and_extension}'
    
        # Return the uploaded image file as a response
        return FileResponse(image_full_path, media_type=f"image/{file_extension}", headers={"Content-Disposition": f"attachment; filename={os.path.basename(image_full_path)}"})
    
    except Exception as e:
        print(f"Error during file upload: {e}")  # Log the error
        return JSONResponse(status_code=400, content={"message": str(e)})

def get_last_alphabetical_dir(base_path):
    dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    if dirs:
        last_dir = sorted(dirs)[-1]  # Sort alphabetically and get the last one
        return os.path.join(base_path, last_dir)
    return None


def get_single_file_name(folder_path):
    # List all items in the folder
    items = os.listdir(folder_path)
    # Filter for files only
    files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]
    # Check if there's exactly one file
    return files[0]  # Return the single file name
