from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil

import cv2
from FDimage import face_det
from FRvideo import face_rec

from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/home", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})

@app.get("/project_details", response_class=HTMLResponse)
async def project_details_page(request: Request):
    return templates.TemplateResponse("project_details.html",{"request": request})

@app.get("/project", response_class=HTMLResponse)
async def project_page(request: Request):
    return templates.TemplateResponse("project.html",{"request": request})

@app.get("/face_detection", response_class=HTMLResponse)
async def project_page(request: Request):
    return templates.TemplateResponse("face_detection.html",{"request": request})

@app.post("/uploadforFD")
async def FDimage(uploadFDimg: UploadFile = File(...)):
    filename = "uploadFDimg."+uploadFDimg.content_type.split("/")[1]
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(uploadFDimg.file, buffer)
	
    detected_image = face_det(filename)
    cv2.imwrite('detected_image.jpg', detected_image)
    return FileResponse('detected_image.jpg')

@app.post("/uploadforFR")
async def FRimage(name: str = Form(...), uploadFRimg: UploadFile = File(...)):

    filename = "uploadFRimg."+uploadFRimg.content_type.split("/")[1]
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(uploadFRimg.file, buffer)
        
    # Write-Overwrites
    file1 = open("name.txt","w") #write mode
    file1.write(name)
    file1.close()
        
    return RedirectResponse("http://192.168.43.87:5000/show")
    
@app.get("/face_recognition", response_class=HTMLResponse)
async def project_page(request: Request):
    return templates.TemplateResponse("face_recognition.html",{"request": request})

@app.get("/about_us", response_class=HTMLResponse)
async def project_page(request: Request):
    return templates.TemplateResponse("about_us.html",{"request": request})
 
