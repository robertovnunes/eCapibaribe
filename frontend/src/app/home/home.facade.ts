import { Injectable } from '@angular/core';
import { HomeState } from './state/home.state';
import { HomeApi } from './api/home.api';
import { Category } from './types/category';
import { first } from 'rxjs';

@Injectable()
export class HomeFacade {
    constructor(
        private readonly homeState: HomeState,
        private readonly homeApi: HomeApi
    ) {}
    public async addCategory(category: Category) {
        await this.homeApi
            .addCategory(category)
            .pipe(first())
            .subscribe({
                next: (categories: Category[]) => {
                    // TODO: remove this line when backend is ready
                    categories.push(category);

                    if (categories.includes(category)) {
                        this.homeState.setCategories(categories);
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

    public async fetchCategories() {
        await this.homeApi
            .fetchCategories()
            .pipe(first())
            .subscribe({
                next: (categories: Category[]) => {
                    this.homeState.setCategories(categories);
                },
                error: error => {
                    // TODO: handle error
                },
            });
    }
}
