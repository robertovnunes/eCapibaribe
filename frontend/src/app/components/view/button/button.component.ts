import {Component, EventEmitter, Input, Output} from '@angular/core';

@Component({
  selector: 'app-button',
  templateUrl: './button.component.html',
  styleUrls: ['./button.component.css']
})
export class ButtonComponent {
     @Input() buttonText!: string;
     @Input() inputbuttonType = '';
     @Input() buttonDisable: boolean = false;
     @Output() buttonAction: EventEmitter<void> = new EventEmitter();
     buttonType = this.inputbuttonType === 'submit'? 'submit' : 'button'
        constructor() {}

        ngOnInit(): void {

        }
}
