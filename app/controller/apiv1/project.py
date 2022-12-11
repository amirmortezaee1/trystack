from app.crud.project import get_items, create_item, get_item_by_name, get_item_by_id
from fastapi import HTTPException
from app.util import now
    
class ProjectController:
     def get_projects(self,skip, limit, db):
          items = get_items(db,  skip=skip, limit=limit)
          return items
 
     def get_project(self,item_id ,db):
          db_item = get_item_by_id(db, id=item_id)
          if db_item is None:
               raise HTTPException(status_code=400, detail="item not find")
          return db_item

     def create_project(self, name, db):
          db_item = get_item_by_name(db , name=name)
          if db_item is not None: 
               raise HTTPException(status_code=400, detail="The name already used.")
          return create_item(db=db, name=name)
          
     def update_project(self ,item_id, status, db):
          db_item = get_item_by_id(db, item_id)
          if db_item is None:
               raise HTTPException(status_code=400, detail="item not find")
          db_item.status = status
          db_item.last_updated_at = now()
          db.commit()
          return f"status change to {status}"

     def delete_project(self , item_id, db):
          db_item= get_item_by_id(db, item_id)
          if db_item is None:
               raise HTTPException(status_code=400, detail="item not find")
          db.delete(db_item)
          db.commit()
          return f"item with id({item_id}) deleted"