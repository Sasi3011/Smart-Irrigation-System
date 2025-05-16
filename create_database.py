"""
Script to explicitly create the irrigation_system database in MongoDB
"""
import pymongo
from pymongo import MongoClient
import datetime

def create_irrigation_database():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Access the irrigation_system database (this will create it if it doesn't exist)
        db = client.irrigation_system
        
        # MongoDB doesn't actually create the database until you add data to it
        # So we'll create a collection and insert a document
        db.system_info.insert_one({
            'name': 'Smart Irrigation System',
            'version': '1.0',
            'created_at': datetime.datetime.now(),
            'description': 'Database for storing irrigation system data'
        })
        
        # Create the collections we need for our application
        db.create_collection('crops')
        db.create_collection('soils')
        db.create_collection('irrigation_logs')
        
        print(f"Successfully created MongoDB database: {db.name}")
        print(f"Collections created: {db.list_collection_names()}")
        print(f"All databases on server: {client.list_database_names()}")
        
        return True
    except Exception as e:
        print(f"Error creating MongoDB database: {str(e)}")
        return False

if __name__ == "__main__":
    create_irrigation_database()
