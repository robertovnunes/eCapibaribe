import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HomeFacade } from '../../home.facade';
import { Category } from '../../types/category';

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

    async createCategory(category: Category) {
        await this.facade.addCategory(category);
    }

    loadCTM() {
        console.log('loadCTM');
        this.router.navigate(['/categories']);
    }
}
