import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HomeComponent } from './home.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { HomeFacade } from '../../home.facade';
import { HomeState } from '../../state/home.state';
import { HomeApi } from '../../api/home.api';

describe('HomeComponent', () => {
    let component: HomeComponent;
    let fixture: ComponentFixture<HomeComponent>;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [HomeComponent],
            providers: [HomeFacade, HomeState, HomeApi],
            imports: [HttpClientTestingModule],
        });
        fixture = TestBed.createComponent(HomeComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
