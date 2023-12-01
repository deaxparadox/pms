import { Component } from '@angular/core';
import { Task } from 'src/app/config.service';
import { Heading } from 'src/app/heading';
import { HeadingService } from 'src/app/heading.service';

@Component({
  selector: 'app-center',
  templateUrl: './center.component.html',
  styleUrls: ['./center.component.css']
})
export class CenterComponent {
  task: Task | undefined;

  title = 'frontend';

  constructor(private httpClientHeading: HeadingService) {}

  headings?: Heading[];

  ngOnInit(): void {
    this.httpClientHeading.getHeadings().subscribe(headings => {
      console.log(headings)
      this.headings = headings
    });
  }

  showTask() {
    // this.configService.
  }
}
