import { Injectable } from '@angular/core';
import { User } from '../interfaces/user';

import { HttpClient } from "@angular/common/http";
import {Observable} from "rxjs";


class dataResponse {
  message = '';
  status_code = '';
  data!: User;
}

@Injectable({
  providedIn: 'root'
})
export class UserloginService {
  private apiUrl = "http://127.0.0.1:8000/users/username?username=";
  constructor(private http: HttpClient) { }

  getUser(value: string | null): Observable<dataResponse> {
    let response = this.http.get<dataResponse>(this.apiUrl+value!.toString());
    response.subscribe(dataresponse => {
      if(dataresponse.status_code != '200') {
        dataresponse.data = {} as User;
      }
    })

    return response;
  }
}
