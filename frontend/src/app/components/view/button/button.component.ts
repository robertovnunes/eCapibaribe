import {Component, EventEmitter, Input, Output} from '@angular/core';

@Component({
  selector: 'app-button',
  templateUrl: './button.component.html',
  styleUrls: ['./button.component.css']
})
export class ButtonComponent {
     @Input() buttonText!: string;
     @Input() inputbuttonType!: string;
     @Input() buttonDisable: boolean = false;
     @Input() btnClick!: string;
     @Output() buttonAction = new EventEmitter();
     buttonType = this.inputbuttonType === 'submit'? 'submit' : 'button'


        constructor() {
        }

        ngOnInit(): void {
        }
}
