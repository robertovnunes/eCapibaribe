import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Item } from '../types/items';

@Injectable()
export class ItemsApi {

  constructor(private http: HttpClient) { }

  public cadastrarItem(item: Item){
    return this.http.post("/api/items", item);
  }
  public getitems(userCPF: string = "123.456.789-10"){
    return this.http.get(`/api/items/${userCPF}`);
  }
}
