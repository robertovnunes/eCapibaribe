import { Component, EventEmitter, Input } from '@angular/core';
import { Item } from '../../types/item';

@Component({
    selector: 'app-list-itens',
    templateUrl: './list-itens.component.html',
    styleUrls: ['./list-itens.component.scss'],
})
export class ListItemsComponent {
    @Input() itens: Item[] | null = [];
}
