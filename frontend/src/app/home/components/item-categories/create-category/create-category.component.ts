import { Component } from '@angular/core';

@Component({
    selector: 'app-create-category',
    templateUrl: './create-category.component.html',
    styleUrls: ['./create-category.component.scss'],
})
export class CreateCategoryComponent {
    public name = '';
    public description = '';
    public keywords = '';
    public imageUrl = '';

    public createCategory(): void {}
}
