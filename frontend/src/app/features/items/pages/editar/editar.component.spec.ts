import { ComponentFixture, TestBed } from '@angular/core/testing';

<<<<<<<< HEAD:frontend/src/app/components/home/home.component.spec.ts
import { HomeComponent } from './home.component';

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HomeComponent]
    });
    fixture = TestBed.createComponent(HomeComponent);
========
import { EditarComponent } from './editar.component';

describe('EditarComponent', () => {
  let component: EditarComponent;
  let fixture: ComponentFixture<EditarComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditarComponent]
    });
    fixture = TestBed.createComponent(EditarComponent);
>>>>>>>> 26c6c9f2c1e4e008de0c480ccf9fa4bb2b1eafc1:frontend/src/app/features/items/pages/editar/editar.component.spec.ts
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
