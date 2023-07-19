import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Item } from '../types/item';

@Injectable()
export class HomeState {
    private readonly items = new BehaviorSubject<Item[]>([]);

    public getItems() {
        return this.items.asObservable();
    }

    public setItems(items: Item[]) {
        this.items.next(items);
    }

    public addItem(item: Item) {
        this.items.next([...this.items.value, item]);
    }
}
