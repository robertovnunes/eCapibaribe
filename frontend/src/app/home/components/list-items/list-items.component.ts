import { Component, EventEmitter, Input } from '@angular/core';
import { Item } from '../../types/item';

@Component({
    selector: 'app-list-items',
    templateUrl: './list-items.component.html',
    styleUrls: ['./list-items.component.scss'],
})
export class ListItemsComponent {
    @Input() items: Item[] | null = [];
}
