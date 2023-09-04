import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Item } from '../types/item';
import {Category} from "../types/category";

@Injectable()
export class HomeState {
    private readonly itens = new BehaviorSubject<Item[]>([]);

    public getItems() {
        return this.itens.asObservable();
    }

    public setCategories(categories: Category[]) {
        this.itens.next(categories);
    }

    public addItem(item: Item) {
        this.itens.next([...this.itens.value, item]);
    }
}
