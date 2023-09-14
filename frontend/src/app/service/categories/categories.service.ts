import {Injectable} from '@angular/core';


import {Category} from "../interfaces/category";

import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

class categoriesResponse {
  message: string = '';
  status_code: string = '';
  data: Category[] = []
}

class categoryResponse{
  message: string = '';
  status_code: string = '';
  data!: Category;
}

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {
  
  private apiUrl = "http://127.0.0.1:8000/categories/"
  constructor(private http: HttpClient) { }

  getCategory(category_id: number) {
    return this.http.get<categoriesResponse>(this.apiUrl + category_id);
  }


  removeCategory(id: number): Observable<categoriesResponse> {
    let result = confirm("tem certeza que deseja remover a categoria?");
    if (result){
      console.log(id)
      return this.http.delete<categoriesResponse>(this.apiUrl+id);
    } else {
      return this.http.get<categoriesResponse>(this.apiUrl);
    }
  }

  editCategory(id: number , newCategory: Category): Observable<categoriesResponse> {
    let result = confirm("tem certeza que deseja atualizar a categoria?");
    /*
    let newCategory: Category;
    newCategory = {} as Category;
    
    newCategory.name = "my categorie new name";
    newCategory.description = "my categorie new name";
    newCategory.keywords = [ "my categorie new name"];
    newCategory.image = "my categorie new name";
    newCategory.items = [];

    console.log(id)
    */
    if (result){
      return this.http.put<categoriesResponse>(this.apiUrl + id, newCategory);
    } else {
      return this.http.get<categoriesResponse>(this.apiUrl);
    }


  }

  Category(id: number): Observable<categoriesResponse> {
    let result = confirm("tem certeza que deseja remover a categoria?");
    if (result){
      return this.http.delete<categoriesResponse>(this.apiUrl+id);
    } else {
      return this.http.get<categoriesResponse>(this.apiUrl);
    }
  }

  getCategories() {
    return this.http.get<categoriesResponse>(this.apiUrl);

  }

  addCategory(newCategory: Category) {
    return this.http.post<categoriesResponse>(this.apiUrl, newCategory);
  }
}
