import { Component, Input } from '@angular/core';

@Component({
    selector: 'app-button',
    templateUrl: './button.component.html',
    styleUrls: ['./button.component.scss'],
})
export class ButtonComponent {
    @Input() type = 'btn large';
    @Input() label = 'Button';
    @Input() disabled = false;
}
