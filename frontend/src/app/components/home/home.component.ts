import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";
import {LocalStorageService} from "../../service/local-storage.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{

  constructor(private router: Router,
              private localStorageService: LocalStorageService) {

  }
  openCTM() {
    this.router.navigateByUrl('/categories').then();
  }

  ngOnInit(): void {
    if (this.localStorageService.get('user') === null) {
      this.router.navigate(['/login']).then();
    }
  }
}
