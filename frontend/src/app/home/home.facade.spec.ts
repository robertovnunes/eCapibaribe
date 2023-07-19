import { HttpClientTestingModule } from '@angular/common/http/testing';
import { HomeFacade } from './home.facade';
import { HomeApi } from './api/home.api';
import { TestBed } from '@angular/core/testing';
import { HomeState } from './state/home.state';

// TODO: fix this test

describe('HomeFacade', () => {
    let facade: HomeFacade;

    it('should create an instance', () => {
        TestBed.configureTestingModule({
            imports: [HttpClientTestingModule],
            providers: [HomeFacade, HomeApi],
        });
        facade = TestBed.inject(HomeFacade);
    });

    it('should be created', () => {
        expect(facade).toBeTruthy();
    });
});
