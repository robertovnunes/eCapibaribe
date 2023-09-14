import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UserService {
    private baseUrl = 'http://localhost:8000'; // Replace with your FastAPI backend URL

    constructor(private http: HttpClient) {}

    registerUser(userData: any): Observable<any> {
        return this.http.post(`${this.baseUrl}/users/register`, userData);
    }
}