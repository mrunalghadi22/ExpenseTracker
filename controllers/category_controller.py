from flask import render_template, request, redirect, url_for, flash, session

from services.category_service import CategoryService
from models.category_model import CategoryModel


class CategoryController:

    @staticmethod
    def index():

        user_id = session.get("user_id")

        categories = CategoryModel.get_categories_by_user(user_id)


        return render_template(
            "category/index.html",
            categories=categories
        )


    @staticmethod
    def create():

        if request.method == "GET":
            return render_template("category/form.html")


        success, message = CategoryService.create_category(
            session["user_id"],
            request.form
        )

        

        if success:
            flash(message, "success")
            return redirect(url_for("category.index"))
        flash(message, "error")
        return render_template(
            
            "category/form.html",
            form=request.form
        )
    
    @staticmethod
    def edit(category_id):

   
     if request.method == "GET":

   
         category = CategoryModel.get_category_by_id(category_id)
    
   
         return render_template(
   
             "category/form.html",
   
             category=category
   
         )

   
     success, message = CategoryService.update_category(
  
     
         session["user_id"],
   
         category_id,
   
         request.form
   
     )

   
     flash(
   
         message,
   
         "success" if success else "error"
   
     )

   
     if success:
   
         return redirect(url_for("category.index"))

   
     category = CategoryModel.get_category_by_id(category_id)

   
     return render_template(
  
          "category/form.html",
   
         category=category
   
     )
    
    @staticmethod
    def delete(category_id):    

        success, message = CategoryService.delete_category(category_id)
    
        flash(
            message,
   
         "success" if success else "error"
        )

        return redirect(
            url_for("category.index")
        )