import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {UserloginService} from "../../service/userlogin/userlogin.service";
import {User} from "../../service/interfaces/user";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  private user!: User;
  usernameInput!: HTMLInputElement | null;
  passwordInput!: HTMLInputElement | null;
  textError!: HTMLParagraphElement | null;

  username: FormControl<string | null>;
  password: FormControl<string | null>;
  form: FormGroup;


  constructor(private readonly fb: FormBuilder,
              private router: Router,
              private userloginService: UserloginService) {
    this.username = this.fb.control('', [Validators.required]);
    this.password = this.fb.control('', [Validators.required]);
    this.form = this.fb.nonNullable.group({
      username: this.username,
      password: this.password,
    });
  }

  ngOnInit() {
    this.usernameInput = document.querySelector('input[name="username"]');
    this.passwordInput = document.querySelector('input[name="password"]');
    this.textError = document.querySelector('.login-error-paragraph');

  }

  countError = 0;


  loginError(mensagem: string) {
    this.usernameInput!.style.borderColor = 'red';
    this.passwordInput!.style.borderColor = 'red';
    this.textError!.textContent = mensagem;
    this.textError!.style.display = 'block';
    alert(mensagem);
    console.log(this.countError);
  }

  doLogin() {
    if (this.form.invalid) {
      this.loginError('Username or Password is empty');
      return false;
    }
    let result = false;
  this.userloginService.getUser(this.username.value).subscribe((u) => this.user = u.data);
    for (let x in this.user) {
      console.log(x);
    }
    console.log(this.username, this.password);
    if (this.username.value === this.user.cpf || this.username.value === this.user.email) {
      result = this.password.value === this.user.senha;
    }

    if (result) {
      alert('Login Successfull');
      this.router.navigateByUrl('/home', {replaceUrl: true}).then(r => console.log(r));
      return true;
    } else {
      if (this.countError < 3){
        this.countError++;
        this.loginError('Username or Password is incorrect');
        alert('Login Failed');
        return false;
      } else {
        setTimeout(() => {
            this.loginError('Username or Password is incorrect 3 times, please wait 30 seconds to retry');
            this.form.disable()
          }
        , 30000);
        return false

      }
    }
  }
}
