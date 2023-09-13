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

  removeCategory(id: number): Observable<categoriesResponse> {
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
