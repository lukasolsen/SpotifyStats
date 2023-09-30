from fastapi import APIRouter, File, UploadFile, Depends
from pathlib import Path
from fastapi.responses import JSONResponse
import zipfile
import os
import tempfile
import shutil
import json
from models.data import DataModel
from models.user import User
from auth.dependencies import get_current_user
from datetime import datetime
from database.database import add_data, get_table

router = APIRouter()


@router.post("/upload")
async def upload_file(in_file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    try:
        # Create a temporary directory to extract the contents of the zip file
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            print(temp_dir_path)

            # Save the uploaded zip file to the temporary directory
            file_path = temp_dir_path / in_file.filename
            print("Temp dir path: ", temp_dir_path, "File path: ", file_path)
            with file_path.open("wb") as file:
                print("Hello World...")
                shutil.copyfileobj(in_file.file, file)

            # Extract the contents of the zip file
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

            # Get a list of extracted file names
            extracted_files = os.listdir(temp_dir)

            my_data_path = temp_dir_path / "MyData"
            data_summary = {"total_seconds_played": 0,
                            "offline_seconds": 0, "online_seconds": 0,
                            "total_tracks": 0, "total_albums": 0, "total_artists": 0,
                            "most_played_track": "", "most_played_track_count": 0}
            data_summary = {
                "user_id": current_user.get("id"),
                "timestamp": datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ'),
                "total_seconds_played": 0,
                "offline_seconds": 0,
                "online_seconds": 0,
                "total_tracks": 0,
                "total_albums": 0,
                "total_artists": 0,
                "tracks": {},
            }

            # Process each JSON file
            tracks = {}

            for file in os.listdir(my_data_path):
                try:
                    # Read the JSON file
                    with open(my_data_path / file, encoding="utf-8", errors='ignore') as f:
                        json_data = json.load(f)

                        for item in json_data:

                            # Add seconds played to online or offline seconds
                            if not item.get("offline"):
                                data_summary["online_seconds"] += item.get(
                                    "ms_played") / 1000
                            else:
                                data_summary["offline_seconds"] += item.get(
                                    "ms_played") / 1000

                            # Add total amounts of tracks, albums and artists
                            data_summary["total_tracks"] += 1
                            data_summary["total_albums"] += 1
                            data_summary["total_artists"] += 1

                            # Add track to tracks dictionary
                            track_id = item.get("spotify_track_uri")
                            if track_id in tracks:
                                tracks[track_id]["count"] += 1
                            else:
                                tracks[track_id] = {"count": 1, "track": item.get(
                                    "master_metadata_track_name")}

                        # Finish the data summary
                        data_summary["total_seconds_played"] += data_summary["online_seconds"] + \
                            data_summary["offline_seconds"]

                        # For the tracks, sort them by count, start with the most played
                        sorted_tracks = sorted(
                            tracks.items(), key=lambda x: x[1]["count"], reverse=True)
                        data_summary["tracks"] = sorted_tracks
                except Exception as e:
                    print(e)
                    pass

            data = DataModel(**data_summary)

            add_data(data=data)

            response_data = {
                "message": "Upload successful",
                "extracted_files": extracted_files,
                "data_summary": data.dict(),
                "tracks": tracks
            }

            return JSONResponse(content=response_data)

    except Exception as e:
        print("Error -> ", e)
        return JSONResponse(content={"message": f"Error: {str(e)}"}, status_code=500)


@router.get("/files/")
async def get_files():
    data = get_table("data")

    return data
