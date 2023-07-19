import { Component } from '@angular/core';
import { Item } from '../../types/item';
import { Router } from '@angular/router';
import { HomeFacade } from '../../home.facade';

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
})
export class HomeComponent {
    constructor(
        private readonly router: Router,
        private readonly facade: HomeFacade
    ) {}

    async createItem(item: Item) {
        await this.facade.addItem(item);
    }

    goToList() {
        this.router.navigate(['/items']);
    }
}
