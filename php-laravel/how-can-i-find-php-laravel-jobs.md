# How can I find PHP Laravel jobs?
// plain

1. The best way to find PHP Laravel jobs is to search for them on job boards such as Indeed, Glassdoor, and Monster.
2. You can also use specialized job search engines such as LaraJobs and Larajobs.co.
3. Additionally, you can use the Laravel framework website itself to find job postings.
4. You can also join the Laravel Slack channel to network with other Laravel developers and find job opportunities.
5. You can also join the Laravel Community and post your resume on their website.
6. You can also attend meetups and conferences related to Laravel and network with people in the industry.
7. Finally, you can also reach out to companies directly and inquire about job openings.

```
<?php

// Example code to find Laravel jobs

$url = "https://www.larajobs.co/jobs/laravel";

$html = file_get_contents($url);

$dom = new DOMDocument();

@$dom->loadHTML($html);

$xpath = new DOMXPath($dom);

$jobs = $xpath->query('//div[@class="job-title"]/a/@href');

foreach ($jobs as $job) {
    echo $job->nodeValue. "\n";
}

```

## Output example


```
/jobs/laravel/senior-laravel-developer-at-acme-corp
/jobs/laravel/backend-developer-at-acme-corp
/jobs/laravel/full-stack-developer-at-acme-corp
```

## Helpful links
- [Indeed](https://www.indeed.com/)
- [Glassdoor](https://www.glassdoor.com/)
- [Monster](https://www.monster.com/)
- [LaraJobs](https://www.larajobs.co/)
- [Larajobs.co](https://larajobs.co/)
- [Laravel Community](https://laravel.com/community)
- [Laravel Slack Channel](https://laravel.com/slack)

onelinerhub: [How can I find PHP Laravel jobs?](https://onelinerhub.com/php-laravel/how-can-i-find-php-laravel-jobs)