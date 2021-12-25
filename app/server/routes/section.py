from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import (
    add_section,
    delete_section,
    retrieve_section,
    retrieve_sections,
    update_section
)
from ..models.section import (
    ErrorResponseModel,
    ResponseModel,
    sectionSchema,
    UpdatesectionModel
)

router = APIRouter()

@router.post("/", response_description="section data added into database")
async def add_section_data(section: sectionSchema = Body(...)):
    section = jsonable_encoder(section)
    new_section = await add_section(section)
    print(new_section)
    return ResponseModel(new_section, "section added successfully")


@router.get("/", response_description="sections retrieved")
async def get_sections():
    sections = await retrieve_sections()
    if sections:
        return ResponseModel(sections, "sections data retrieved successfully")
    return ResponseModel(sections, "Empty list returned")


@router.get("/{id}", response_description="section data retrieved")
async def get_section_data(id):
    section = await retrieve_section(id)
    if section:
        return ResponseModel(section, "section data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "section doesn't exist.")


@router.put("/{id}")
async def update_section_data(id: str, req: UpdatesectionModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_section = await update_section(id, req)
    if updated_section:
        return ResponseModel(
            "section with ID: {} name update is successful".format(id),
            "section name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the section data.",
    )


@router.delete("/{id}", response_description="section data deleted from the database")
async def delete_section_data(id: str):
    deleted_section = await delete_section(id)
    if deleted_section:
        return ResponseModel(
            "section with ID: {} removed".format(id), "section deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "section with id {0} doesn't exist".format(id)
    )