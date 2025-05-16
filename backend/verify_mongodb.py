"""
Script to verify MongoDB connection and create the irrigation_system database
"""
import pymongo
from pymongo import MongoClient
import datetime

def verify_mongodb_connection():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Access the irrigation_system database (will be created if it doesn't exist)
        db = client.irrigation_system
        
        # Create a test document to ensure the database exists
        result = db.connection_test.insert_one({
            'test': 'Connection successful',
            'timestamp': datetime.datetime.now()
        })
        
        # Print connection information
        print(f"Successfully connected to MongoDB")
        print(f"Database name: {db.name}")
        
        # List all collections in the database
        collections = db.list_collection_names()
        print(f"Collections in {db.name}: {collections}")
        
        # List all databases on the server
        databases = client.list_database_names()
        print(f"All databases on server: {databases}")
        
        return True
    except Exception as e:
        print(f"MongoDB connection error: {str(e)}")
        return False

if __name__ == "__main__":
    verify_mongodb_connection()
