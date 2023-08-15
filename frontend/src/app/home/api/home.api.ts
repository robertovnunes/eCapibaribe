import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Item } from '../types/item';
import { Observable, of } from 'rxjs';

@Injectable()
export class HomeApi {
    constructor(private readonly http: HttpClient) {}

    public fetchItems(): Observable<Item[]> {
        // mocked version
        // TODO: remove this when backend is ready
        return of([
            { id: '792', name: 'Naruto com chapéu do Luffy' },
        ] as Item[]);
        // TODO: uncomment this when backend is ready
        // return this.http.get<Item[]>('/itens');
    }

    public addItem(item: Item): Observable<Item[]> {
        // mocked version
        // TODO: remove this when backend is ready
        return of([
            { id: '792', name: 'Naruto com chapéu do Luffy' },
        ] as Item[]);
        // TODO: uncomment this when backend is ready
        // return this.http.post<Item[]>('/itens', item);
    }
}
