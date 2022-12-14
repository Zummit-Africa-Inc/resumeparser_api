import os
import time

from fastapi import FastAPI, File, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse, StreamingResponse
from resume_parser import resumeparse
from pdfminer.pdfparser import PDFSyntaxError

app = FastAPI(
    title="Resume Parser API",
    description="""An API for parsing resumes and extracting information from them.""",
    version="0.0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
    ResumeParser API 📚
    A Resume Information Parser using FastAPI!
    Note: add "/redoc" to get the complete documentation.
    """
    return note


@app.post("/parse", tags=["Parser"])
async def resume_parser(file: UploadFile) -> dict:
    """
    The resume_parser function takes a file path to a resume as an argument and returns the parsed data as a dictionary.
    The returned dictionary contains the following fields:
    name, email, phone_number, work_experience (a list of dictionaries), skills (a list).
    Args:
        file:UploadFile: Pass the file that is uploaded to the function
    Returns:
        A string of the file name
    """
    # write a function to save the uploaded file and return the file name
    files = await file.read()
    # save the file
    filename = "file.pdf"
    with open(filename, "wb+") as f:
        f.write(files)
    # open the file and return the file name
    try:
        with open(filename, "rb") as f:
            pdf = f.read()
        data = data = resumeparse.read_file(filename)
        time.sleep(1)
        filepath = "file.pdf"
        if os.path.exists(filepath):
            os.remove(filepath)
        return data
        

    except (FileNotFoundError, PDFSyntaxError) as e:
        return f"Error! Cannot Parse Resume. Please make sure you upload a PDF File!"
