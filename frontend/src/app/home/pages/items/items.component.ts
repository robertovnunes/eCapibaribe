import { Component } from '@angular/core';
import { Item } from '../../types/item';
import { Observable } from 'rxjs';
import { HomeFacade } from '../../home.facade';
import { Router } from '@angular/router';

@Component({
    selector: 'app-itens',
    templateUrl: './itens.component.html',
    styleUrls: ['./itens.component.scss'],
})
export class ItemsComponent {
    itens$: Observable<Item[]> = new Observable<Item[]>();

    constructor(private readonly facade: HomeFacade, private router: Router) {
        this.itens$ = this.facade.getItems();
    }

    goToHome() {
        this.router.navigate(['/']);
    }
}
