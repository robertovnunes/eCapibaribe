import { Component } from '@angular/core';
import { Item } from '../../types/item';
import { Observable } from 'rxjs';
import { HomeFacade } from '../../home.facade';
import { Router } from '@angular/router';

@Component({
    selector: 'app-items',
    templateUrl: './items.component.html',
    styleUrls: ['./items.component.scss'],
})
export class ItemsComponent {
    items$: Observable<Item[]> = new Observable<Item[]>();

    constructor(private readonly facade: HomeFacade, private router: Router) {
        this.items$ = this.facade.getItems();
    }

    goToHome() {
        this.router.navigate(['/']);
    }
}
