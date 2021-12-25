from bson.objectid import ObjectId
import motor.motor_asyncio
from decouple import config
MONGO_LOCALHOST = "mongodb://localhost:27017" 
MONGO_ATLAS="mongodb+srv://khairi:khairi@cluster0.a384h.mongodb.net/test?authSource=admin&replicaSet=atlas-dxe09u-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_LOCALHOST)
database = client.Classes
student_collection = database.get_collection("Students")
section_collection = database.get_collection("Sections")
student_collection.create_index([('fullname', 'text')])
section_collection.create_index([('section_name', 'text')])
def student_helper(student):
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "section": student["section"],
        "year": student["year"],
    }


# Retrieves all the students in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student to database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrive a student with matching id
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with maching ID
async def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True 

#### Sections

def section_helper(section):
    return {
        "id": str(section["_id"]),
        "section_name": section["section_name"],
        "hours": section["hours"],
    }


# Retrieves all the sections in the database
async def retrieve_sections():
    sections = []
    async for section in section_collection.find():
        sections.append(section_helper(section))
    return sections


# Add a new section to database
async def add_section(section_data: dict) -> dict:
    section = await section_collection.insert_one(section_data)
    new_section = await section_collection.find_one({"_id": section.inserted_id})
    return section_helper(new_section)


# Retrive a section with matching id
async def retrieve_section(id: str) -> dict:
    section = await section_collection.find_one({"_id": ObjectId(id)})
    if section:
        return section_helper(section)


# Update a section with maching ID
async def update_section(id: str, data: dict):
    if len(data) < 1:
        return False
    section = await section_collection.find_one({"_id": ObjectId(id)})
    if section:
        updated_section = await section_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_section:
            return True
        return False


# Delete a section from database
async def delete_section(id: str):
    section = await section_collection.find_one({"_id": ObjectId(id)})
    if section:
        await section_collection.delete_one({"_id": ObjectId(id)})
        return True 