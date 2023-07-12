import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent {
  @Input() username: string = '';
  @Input() password: string = '';

  constructor() { }

  ngOnInit(): void {
  
  }


}
