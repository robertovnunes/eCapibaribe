import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Category } from '../types/category';
import { Observable } from 'rxjs';

@Injectable()
export class HomeApi {
    constructor(private readonly http: HttpClient) {}

    public fetchCategories(): Observable<Category[]> {
        return this.http.get<Category[]>('/categories');
    }

    public addCategory(category: Category): Observable<Category[]> {
        // TODO: uncomment this when backend is ready
        return this.http.post<Category[]>('/categories', category);
    }
}
