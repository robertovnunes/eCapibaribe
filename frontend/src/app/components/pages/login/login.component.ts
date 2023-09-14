import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {UserloginService} from "../../../service/userlogin/userlogin.service";
import {User} from "../../../service/interfaces/user";
import {LocalStorageService} from "../../../service/local-storage.service";


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

  countError!: number;
  time!: number;


  constructor(private readonly fb: FormBuilder,
              private router: Router,
              private userloginService: UserloginService,
              private localStorageService: LocalStorageService) {
    this.localStorageService.set('user', null);
    this.username = this.fb.control('', [Validators.required]);
    this.password = this.fb.control('', [Validators.required]);
    this.form = this.fb.nonNullable.group({
      username: this.username,
      password: this.password,
    });
    this.countError = 0;
  }

  ngOnInit() {
    this.usernameInput = document.querySelector('input[name="username"]');
    this.passwordInput = document.querySelector('input[name="password"]');
    this.textError = document.querySelector('.login-error-paragraph');
    this.clear();
  }


  loginError(mensagem: string) {
    this.usernameInput!.style.borderColor = 'red';
    this.passwordInput!.style.borderColor = 'red';
    this.textError!.textContent = mensagem;
    alert(mensagem);
    this.textError!.style.display = 'block';
  }

  loginDisabled() {
    this.time = 20
    let message = 'Login disabled for ' + this.time.toString() + ' seconds'
    alert(message);
    let timer = setInterval(() => {
      if (this.time > 0) {
        this.form.disable();
        message = 'Login disabled for ' + this.time.toString() + ' seconds';
        this.textError!.textContent = message;
        this.textError!.style.display = 'block';
        this.time--;
      } else {
        clearInterval(timer);
        this.usernameInput!.style.borderColor = this.passwordInput!.style.borderColor = 'black';
        this.textError!.style.display = 'none';
        this.form.enable();
        this.clear();
        alert('Login enabled');
      }
    }, 1000);
    this.countError = 0;
    this.router.navigateByUrl('/login', {replaceUrl: true}).then();

  }

  doLogin() {
    if (this.form.invalid) {
      this.loginError('Username or Password is empty');
      this.countError++;
      if (this.countError === 3) {
        this.loginDisabled();
      }
      return false;
    }
    let result = false;
    try {
      this.userloginService.getUser(this.username.value).subscribe(u => {
        this.user = u.data;
      });
    } catch (e) {
      if (e instanceof Error) {
        return false;
      }
    }
    if ((this.username.value === this.user.cpf) || (this.username.value === this.user.email)) {
      result = this.password.value === this.user.senha;
    } else {
      result = false;
    }
    if (result) {
      this.localStorageService.set('user', this.user);
      this.router.navigateByUrl('/home', {replaceUrl: true}).then();
      return true;
    } else {
      this.localStorageService.set('user', null);
      if (this.countError === 3) {
        this.loginDisabled();
      } else {
        this.countError++;
        this.loginError('Username or Password is incorrect');
        alert('Login Failed');
      }

      return false;
    }
  }

  clear() {
    this.form.reset();
  }

  enterSubmit(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      this.doLogin();
    }
  }

}
