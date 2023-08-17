import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Item } from '../types/item';

@Injectable()
export class HomeState {
    private readonly itens = new BehaviorSubject<Item[]>([]);

    public getItems() {
        return this.itens.asObservable();
    }

    public setItems(itens: Item[]) {
        this.itens.next(itens);
    }

    public addItem(item: Item) {
        this.itens.next([...this.itens.value, item]);
    }
}
