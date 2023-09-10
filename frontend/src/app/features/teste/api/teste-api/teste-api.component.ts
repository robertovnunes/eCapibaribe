import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../../types/users/user';

@Injectable()

export class TesteApi {
    
    constructor(private http: HttpClient) { }

    public postRegister(user: User){
        this.http.post("/api/users/register", user).subscribe((response)=>console.log(response));
    }
}
