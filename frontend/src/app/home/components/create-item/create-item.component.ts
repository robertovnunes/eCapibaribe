import { Component, EventEmitter, Output } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Item } from '../../types/item';

@Component({
    selector: 'app-create-item',
    templateUrl: './create-item.component.html',
    styleUrls: ['./create-item.component.scss'],
})
export class CreateItemComponent {
    @Output() createItemEvent: EventEmitter<Item> = new EventEmitter<Item>();
    @Output() goToListEvent = new EventEmitter();

    form: FormControl = new FormControl('');

    public createItem(): void {
        if (this.form.value === '' || this.form.value === null) {
            alert('Por favor, escreva um nome válido.');
            return;
        }

        const item: Item = {
            id: Date.now().toString().slice(-3),
            name: this.form.value,
        };

        this.createItemEvent.emit(item);
    }

    public goToList() {
        this.goToListEvent.emit();
    }
}
