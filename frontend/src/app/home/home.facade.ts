import { Injectable } from '@angular/core';
import { HomeState } from './state/home.state';
import { HomeApi } from './api/home.api';
import { Item } from './types/item';
import { first } from 'rxjs';

@Injectable()
export class HomeFacade {
    constructor(
        private readonly homeState: HomeState,
        private readonly homeApi: HomeApi
    ) {}

    public getItems() {
        return this.homeState.getItems();
    }

    public async fetchItems() {
        await this.homeApi
            .fetchItems()
            .pipe(first())
            .subscribe({
                next: (itens: Item[]) => {
                    this.homeState.setItems(itens);
                },
                error: error => {
                    // TODO: handle error
                },
            });
    }

    public async addItem(item: Item) {
        await this.homeApi
            .addItem(item)
            .pipe(first())
            .subscribe({
                next: (itens: Item[]) => {
                    // TODO: remove this line when backend is ready
                    itens.push(item);

                    if (itens.includes(item)) {
                        this.homeState.setItems(itens);
                        alert('Item criado com sucesso!');
                    } else {
                        alert('Erro ao criar item!');
                    }
                },
                error: error => {
                    // TODO: handle error
                },
            });
    }
}
