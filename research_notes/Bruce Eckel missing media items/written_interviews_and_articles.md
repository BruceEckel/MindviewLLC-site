# Written interviews, profiles, reviews, and outside articles by or about Bruce Eckel that are missing from the media page

Research date: 2026-11-22.
Compared against `content/media/index.md` and `content/bibliography/index.md`.

Verification labels used below:

- **verified by fetch**: I fetched the page (WebFetch or curl) and read the title, author, and date from it.
- **status 200 only**: curl returned HTTP 200 for the URL, but I did not read the content (the site blocks the fetch tool, or the page is rendered by JavaScript).
- **search results only**: the URL and details come from a search result snippet; I did not fetch the page.

Tool limits that shaped the results:
the fetch tool cannot open `web.archive.org`, so Wayback snapshots were checked with curl;
`blogs.oracle.com` and `blog.jetbrains.com` return 403 to automated clients;
the Internet Archive went "Temporarily Offline" partway through the session, so a few Wayback lookups returned nothing.

## Which written interviews exist?

### Takeaway
Seven written items are missing from the media page: three more parts of the 2003 Artima conversation with Bill Venners, a 2003 Borland Developer Network interview by Clay Shannon, the full written transcript of the 2021 Leanpub interview, a Japanese InfoQ translation of the 2009 interview, and the written text of the 2013 James Ward interview (the link on the page is dead).
I found no written interview on JAXenter, DZone, Java Code Geeks, The Register, Stepik, Medium, Hacker Noon, dev.to, CSDN, Habr, or Polish and Brazilian sites; the searches for those returned only items already listed.

### Cited Findings

Missing written interviews, confirmed:

- **June 2003. "The Zen of Python: A Conversation with Bruce Eckel, Part II."** Artima Developer. By Bill Venners. Dated June 23, 2003 on the page. URL: https://www.artima.com/articles/the-zen-of-python (status 200 only at this address; the content was verified by fetch at the older address https://www.artima.com/intv/prodperf.html, whose internal links point to `/articles/the-zen-of-python`).
- **July 2003. "Type Checking and Techie Control: A Conversation with Bruce Eckel, Part III."** Artima Developer. By Bill Venners. Dated July 7, 2003. URL: https://www.artima.com/articles/type-checking-and-techie-control (verified by fetch).
- **July 2003. "Python and the Tipping Point: A Conversation with Bruce Eckel, Part IV."** Artima Developer. By Bill Venners. Dated July 21, 2003. URL: https://www.artima.com/intv/tippingP.html (verified by fetch). The newer address https://www.artima.com/articles/python-and-the-tipping-point returns 200 (status 200 only).
- Part I of that series, "Python and the Programmer" (June 2, 2003), is the one item the media page already lists. Part IV says the next installment in the Artima series is an interview with Elliotte Rusty Harold, so the Eckel conversation has four parts. (Source: https://www.artima.com/intv/tippingP.html)
- **July 2003 (approx.). "Interview with Bruce Eckel by Clay Shannon."** Borland Developer Network (community.borland.com). Interviewer: Clay Shannon. Topics per a contemporary summary: C# as "a better Java", a wish for a Python IDE from Borland, doubts about Mono, Python as a first teaching language. The original address `http://community.borland.com/article/0,1410,30139,00.html` is gone. Wayback copy: http://web.archive.org/web/20080517031942/http://community.borland.com/article/0,1410,30139,00.html (verified by fetch with curl; page title reads "Interview with Bruce Eckel by Clay Shannon"). I did not extract the publication date from the snapshot. Two blog posts that link to it are dated July 22, 2003 and July 31, 2003, so the interview is from July 2003 or shortly before. (Sources: https://simonwillison.net/2003/Jul/22/bruceEckel/ and https://blog.sidneidasilva.com/2003/07/31/interview-with-bruce-eckel-by-clay-shannon/, both verified by fetch)
- **February 2021. "Bruce Eckel, Co-Author of Atomic Kotlin."** The Leanpub Podcast (Frontmatter), episode 192. Interviewer: Len Epp. Published February 2, 2021; recorded January 11, 2021. The page carries a full written transcript, so it counts as a written interview as well as audio. URL: https://leanpub.com/podcasts/leanpub/bruce-eckel-02-02-21 (verified by fetch). This is the same episode as the "February 2021 Interview on Frontmatter Podcast" entry whose Stitcher link is dead, so it is a replacement link more than a new item.
- **May 2009. "Bruce Eckel氏、Python、Java、Flex、RIAについて語る."** InfoQ Japan. Original by Jon Rose, translated by 能仁 信亮. Page date May 31, 2009. Japanese translation of the InfoQ item already listed ("Python, Java, Flex, and RIAs"). URL: https://www.infoq.com/jp/news/2009/05/bruce-eckel/ (verified by fetch).
- **July 2013. "Bruce Eckel on Learning Scala and Tech Conferences."** Typesafe blog (later Lightbend). Interviewer: James Ward. Dated July 8, 2013. This is a written conversation about Atomic Scala and the Scala Summit; the snapshot contains no YouTube or Vimeo embed. The media page lists it as "2013 Interview with James Ward" with a dead Lightbend URL. Wayback copy: http://web.archive.org/web/20150907021510/https://www.typesafe.com/blog/bruce-eckel-on-learning-scala-and-tech-conferences (verified by fetch with curl).

Details for interviews already listed that the media page could correct:

- The JavaWorld interview "Eckel thinks in Java" is by John Zukowski and is dated June 8, 2001. It now lives at InfoWorld. (Source: https://www.infoworld.com/article/2161387/eckel-thinks-in-java.html, verified by fetch)
- The InformIT "Interview with Bruce Eckel" is dated Sep 21, 2001. (Source: http://web.archive.org/web/20250326021354/https://www.informit.com/articles/article.aspx?p=23416, verified by fetch with curl)
- The InformIT item "Is This the Best We Can Do? A Conversation with Bruce Eckel, Part I" is dated May 18, 2007, and a search snippet describes it as a podcast with Greg Doench of Pearson. (Source: http://web.archive.org/web/20250513191100/https://www.informit.com/articles/article.aspx?p=762675, verified by fetch with curl)

Audio and video items that surfaced and are not on the media page (out of scope here; passed along for the other researchers, none fetched by me unless noted):

- October 2024, A Bootiful Podcast (Josh Long), "Bruce Eckel, 'Thinking in Java' author and one of the most influential authors in my career", recorded live at Dev2Next. https://bootifulpodcast.podbean.com/e/bruce-eckel-thinking-in-java-author-and-one-of-the-most-influential-authors-in-my-career/ (search results only)
- November 2025, A Bootiful Podcast, "The legendary Bruce Eckel on language design, effects, abstraction, concurrency, and so much more", posted November 13, 2025. https://spring.io/blog/2025/11/13/a-bootiful-podcast-bruce-eckel/ (search results only)
- January 2026, GOTO Book Club, "Effect Oriented Programming", Bill Frasure, Bruce Eckel, and James Ward with Andrew Harmel-Law. https://gotopia.tech/episodes/420 (search results only; one podcast listing shows a February 24 date, so the month is uncertain)
- 2026, PyCon US 2026, Paul Everitt interview, "Bruce Eckel on Free-Threaded Python, Type Checking, and Programming in the AI Era". https://www.youtube.com/watch?v=hj6RiSEUuoY (search results only)
- October 2019, The 6 Figure Developer Podcast, episode 111, "Atomic Kotlin and Teal Orgs with Bruce Eckel". https://dev.to/6figuredev/episode-111-atomic-kotlin-and-teal-orgs-with-bruce-eckel (search results only)

### Inferences
- The Artima interview index dates the whole Eckel conversation "August 2002", while each article page carries a June or July 2003 date. The article pages are the primary record, so the 2003 dates are the ones to use; "August 2002" is probably when the conversation was recorded. (Sources: https://www.artima.com/intv/ and https://www.artima.com/articles/type-checking-and-techie-control)
- The LinkedIn post "Interview of Bruce Eckel" by Anuva Ambastha is almost certainly a repost of the 2015 opensource.com interview already listed, since a search snippet names the same interviewer and topics. LinkedIn returned 403, so I did not confirm this. (https://www.linkedin.com/pulse/interview-bruce-eckel-anuva-ambastha, search results only)

### Gaps
- Chinese sites: two searches (English and Chinese keywords, including "专访" and "采访") found no InfoQ China, CSDN, or other Chinese written interview beyond the July 2022 WeChat item already listed. US-only search is weak for Chinese sites, so this is "not found", not "does not exist".
- Russian (Habr), Polish, and Brazilian sites: one search each direction returned nothing about Eckel. The one Habr hit was an interview with Venkat Subramaniam.
- JAXenter, DZone, Java Code Geeks, Stepik, Medium, Hacker Noon, dev.to, Mouse vs Python (beyond the listed PyDev of the Week), Dr. Dobb's interviews: a combined search returned no written interview. I did not run each site's own search.
- I did not extract the exact date of the Borland interview from the Wayback snapshot.
- The 2003 eight-part Artima interview with Anders Hejlsberg has Eckel as co-interviewer with Bill Venners. It is by him, not about him, and I did not list its parts. Index: https://www.artima.com/intv/anders.html (search results only).

## Which notable reviews or coverage of his books and projects exist in publications?

### Takeaway
Four pieces of published coverage are missing from the media page: The Register's 2006 review of Thinking in Java 4th edition, LWN's 2000 review of the first edition, the 2003 Jolt Awards article in Software Development (hosted by Dr. Dobb's) naming Thinking in Java 3rd edition, and a 2021 JetBrains Kotlin blog post that features Atomic Kotlin.
I found no review of Atomic Kotlin, Effect Oriented Programming, or On Java 8 in Java Magazine (beyond the listed one), InfoQ, JavaWorld, or Slashdot.

### Cited Findings
- **April 2006. "Thinking in Java, new 4th Ed."** The Register. Reviewer: Dr Pan Pantziarka. Dated April 7, 2006. A review of the 4th edition; verdict: a great book for experienced programmers moving to Java, not a first book for beginners. URL: https://www.theregister.com/software/2006/04/07/thinking-in-java-new-4th-ed/683565 (verified by fetch).
- **April 2000. "Thinking in Java" (LWN Review).** LWN.net. Reviewer: Jeff Berry. Dated April 22, 2000. Reviews the first edition (Prentice Hall, 1998) and mentions the coming second edition. URL: https://static.lwn.net/Reviews/ThinkingInJava.php3 (verified by fetch).
- **June 2003. "The 13th Annual Software Development Jolt & Productivity Awards."** Software Development magazine, archived by Dr. Dobb's. By Rosalyn Lum. Dated June 01, 2003. Under "BOOKS: TECHNICAL" it lists "Thinking in Java (3rd Edition), Bruce Eckel (Prentice Hall, 2002)" and says Eckel "also won a 1995 Jolt Award for his Thinking in C++". The live address `drdobbs.com/joltawards/the-13th-annual-software-development-jol/184414991?pgno=7` no longer resolves (DNS failure). Wayback copy: http://web.archive.org/web/2023/https://www.drdobbs.com/joltawards/the-13th-annual-software-development-jol/184414991?pgno=7 (verified by fetch with curl). The excerpt I read does not say whether the book was the Jolt winner or a Productivity Award winner in that category.
- **April 2021. "Why Learn Kotlin?" (title inferred from the URL slug).** JetBrains Kotlin blog. A search snippet says the post marks the release of Atomic Kotlin and calls it one of JetBrains' favorite resources for learning Kotlin from scratch. URL: https://blog.jetbrains.com/kotlin/2021/04/why-learn-kotlin/ (status 200 only; the fetch tool got 403, so title, author, and exact date are unconfirmed).
- **August 2026. "Thinking in Python: Bruce Eckel Revives His 2008 Book With Claude in 2026."** Developers Digest (developersdigest.tech). No author named. Dated August 24, 2026. Coverage of the free 47-chapter Thinking in Python targeting Python 3.15, its license, and the AI disclosure. URL: https://www.developersdigest.tech/blog/thinking-in-python-bruce-eckel-2026 (verified by fetch). This is a small outlet with an unnamed author, so weigh it as minor coverage.
- **February 2021. "Atomic Kotlin Review."** Personal blog (griffio.github.io), dated February 12, 2021 per its URL. A reader review, not a notable publication; listed for completeness. URL: https://griffio.github.io/kotlin/2021/02/12/Atomic-Kotlin-Review (search results only).
- Award history as reported by secondary sources (Wikipedia and publisher pages, not original announcements): Thinking in C++ won the 1995 Software Development Jolt Award for best book; Thinking in Java won the Java Developer's Journal Editor's Choice Award for Best Book (1998), a Software Development Productivity Award (1999), JavaWorld Reader's Choice (2000) and Editor's Choice (2001) awards, the Jolt Award (2002 or 2003), and JDJ Readers' Choice awards (2003, 2007). (Source: https://en.wikipedia.org/wiki/Thinking_in_Java, search results only)

### Inferences
- The Jolt year conflict (2002 in some sources, 2003 in others) is likely a labeling difference: the 13th Annual awards article is dated June 2003 and covers a book published in 2002. (Source: the Wayback copy of the Dr. Dobb's page above)
- The 1995 Jolt for Thinking in C++ is corroborated by the 2003 Software Development article, which is a publication record and stronger than the bookseller pages.

### Gaps
- No Slashdot book review of any Eckel book turned up in search.
- No InfoQ, JavaWorld, or Java Magazine review of Atomic Kotlin or Effect Oriented Programming turned up. Coverage of Effect Oriented Programming appears to be audio and video only (GOTO Book Club, Bootiful Podcast, Happy Path Programming).
- I found no original announcement pages for the JavaWorld Editors' Choice and Readers' Choice awards, the JDJ awards, or the 1995 and 1999 Software Development awards. Those magazines' archives are mostly offline.
- No C/C++ Users Journal, ACCU, or Linux Journal review was found in one search; ACCU's book review database was not searched directly.

## Which article series did he write for outside publications that the two files do not list?

### Takeaway
Two outside bodies of writing are missing as named entries: the "Computing Thoughts" weblog at Artima (roughly 2003 to November 2014, on the order of 280 posts) and an editor's index to his seven-part 2022 Java Magazine series ("The Eckel Index"), which is a more useful link than the author page the media file points to.
I found no online record of individual articles from the print magazines the bibliography already names (C++ Report, Embedded Systems Programming, Micro Cornucopia, Unix Review, and the rest).

### Cited Findings
- **"Computing Thoughts: A Weblog by Bruce Eckel."** Artima Developer weblogs. The index shows 15 posts per page across 19 pages. The latest post is "Moving This Blog to Github Pages", November 21, 2014; other visible titles include "Markdown vs. AsciiDoc" (July 16, 2014), "Apple's New Swift Language" (June 10, 2014), and "Windows 8 is ... Not So Bad" (April 27, 2013). URL: https://www.artima.com/weblogs/index.jsp?blogger=beckel (verified by fetch). Neither file lists this weblog.
- **July 2022. "The Eckel Index: New language features from Java 9 through Java 17."** Java Magazine (Oracle). By Alan Zeichick, editor in chief, dated July 1, 2022 per a search snippet. It indexes seven articles by Eckel published earlier in 2022 on features added after Java 8 (records in article 2, interfaces and sealed classes in article 3, pattern matching guards and dominance in article 6). URL: https://blogs.oracle.com/javamagazine/post/java-eckel-index (search results only; Oracle returns 403 to automated clients). Wayback copy exists: http://web.archive.org/web/20251015061553/https://blogs.oracle.com/javamagazine/post/java-eckel-index (availability confirmed through the Wayback API; the snapshot body needs JavaScript, so I did not read it).
- **May 2022. "Bruce Eckel on pattern matching in Java."** Java Magazine (Oracle). By Bruce Eckel, dated May 20, 2022 per a search snippet. One of the seven. URL: https://blogs.oracle.com/javamagazine/post/java-pattern-matching (search results only). Wayback: http://web.archive.org/web/20240104173545/https://blogs.oracle.com/javamagazine/post/java-pattern-matching (availability confirmed through the Wayback API). A Japanese translation exists at https://blogs.oracle.com/oracle4engineer/java-pattern-matching-ja (search results only).
- The media page already links the Java Magazine author page, so the series is covered there in general terms. The author page's own bio says he "has published 10 books, numerous blog posts, over 150 articles". (Source: http://web.archive.org/web/20260310125409/https://blogs.oracle.com/authors/bruce-eckel/, verified by fetch with curl; the article list on that snapshot is loaded by JavaScript and was not readable)

### Inferences
- The Artima weblog index shows posts back to January 2012 on its first pages, and search results show Artima-hosted "Computing Thoughts" posts from 2005 ("The departure of the hyper-enthusiasts"). With 19 pages of 15, the weblog likely spans about 2003 to 2014 with up to 285 posts. The start year is not confirmed. (Source: https://www.artima.com/weblogs/index.jsp?blogger=beckel)

### Gaps
- I could not read the titles and dates of all seven 2022 Java Magazine articles; Oracle blocks automated fetches and the Wayback copies are JavaScript shells. A person with a browser can copy them from the Eckel Index page.
- No online index of his print columns (Web Techniques "Java Alley", Unix Review "C++ Adviser", Embedded Systems Programming, Micro Cornucopia, C Gazette, The C++ Report, Computer Language, Midnight Engineering, Dr. Dobb's Journal) was found. These are all named in the bibliography already; individual article titles and dates would need the magazines' scanned archives (archive.org has Micro Cornucopia and Dr. Dobb's scans), which I did not search.
- No Substack, Medium, or dev.to article series under his name was checked beyond one search hit noting a July 2023 bruceeckel.com post titled "Trying Substack".

## Coverage from 2023 through 2026

### Takeaway
Written coverage in this period is thin: the one independent written article I found is the August 2026 Developers Digest piece on Thinking in Python.
Everything else from 2023 to 2026 is audio or video (two Bootiful Podcast episodes, the GOTO Book Club episode, a PyCon US 2026 interview) or self-published.

### Cited Findings
- August 24, 2026: "Thinking in Python: Bruce Eckel Revives His 2008 Book With Claude in 2026", Developers Digest. (Source: https://www.developersdigest.tech/blog/thinking-in-python-bruce-eckel-2026, verified by fetch)
- The GitHub README for Thinking in Python describes the book as "Fluency, Types, and Design: An intermediate/advanced book using Python 3.15". (Source: https://github.com/BruceEckel/ThinkingInPython, search results only)
- Leanpub lists Effect Oriented Programming as complete, last updated 2024-09-17, and a separate TypeScript edition page exists. (Sources: https://leanpub.com/effect-oriented-programming and https://leanpub.com/effect-oriented-programming-typescript, search results only)
- Audio and video from the period are listed under the first question (Bootiful Podcast October 2024 and November 2025, GOTO Book Club January 2026, PyCon US 2026 interview).

### Inferences
- A search across 2025 and 2026 returned no profile or interview in a major publication, so the media page's 2023 to 2026 additions will come almost entirely from the audio and video researchers.

### Gaps
- No written review of Effect Oriented Programming was found anywhere.
- I did not search Hacker News, Reddit, or newsletters (Python Weekly, PyCoder's Weekly, Kotlin Weekly) for mentions, which is where coverage of the 2026 Thinking in Python release would most likely appear.

## Which links in the existing media list are dead, and what replaces them?

### Takeaway
Of 34 URLs, 8 are dead or now land on a generic page, 2 are blocked to automated clients and need a browser check, and 3 redirect to a working new address that should be updated.
The other 21 return 200 at their own address (the `youtu.be` short links redirect to youtube.com as designed).

### Cited Findings

Dead or landing on the wrong page:

- **Frontmatter podcast (Feb 2021)**, `stitcher.com/show/frontmatter/episode/...`: redirects to Pandora's "stitcher-sunset" page. Replacement: https://leanpub.com/podcasts/leanpub/bruce-eckel-02-02-21 (verified by fetch; same episode, with transcript).
- **VJug24 keynote (Nov 2017)**, `virtualjug.com/vjug24-keynote-an-overview-of-kotlin-for-java-programmers/`: no response (connection fails). The Wayback API reports no snapshot of this URL, and a search for a YouTube copy found nothing. No replacement found.
- **Creating Trust Organizations (June 2015)**, `conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/41505`: redirects to the generic https://www.oreilly.com/conferences/ page. Replacement candidate: http://web.archive.org/web/20191120193433/https://conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/41505 (the Wayback API reports a 200 snapshot; the Archive went offline before I could read it, so content is unconfirmed).
- **Interview with James Ward (2013)**, `lightbend.com/blog/bruce-eckel-on-learning-scala-and-tech-conferences`: 404 after a malformed redirect. Replacement: http://web.archive.org/web/20150907021510/https://www.typesafe.com/blog/bruce-eckel-on-learning-scala-and-tech-conferences (verified by fetch with curl; dated July 8, 2013).
- **Reinventing Business at Heroku (May 2012)**, `vimeo.com/herokai/review/40551380/dbcaffb1e2`: 404. The plain address https://vimeo.com/40551380 returns 200, but the page title came back empty, so I could not confirm it is this talk (status 200 only). Check it in a browser.
- **Is This the Best We Can Do? (May 2007)**, `informit.com/articles/article.aspx?p=762675`: redirects to the generic InformIT articles index. Replacement: http://web.archive.org/web/20250513191100/https://www.informit.com/articles/article.aspx?p=762675 (verified by fetch with curl; title "Is This the Best We Can Do? A Conversation with Bruce Eckel, Part I", May 18, 2007).
- **InformIT interview (Sept 2001)**, `informit.com/articles/article.aspx?p=23416`: redirects to the generic InformIT articles index. Replacement: http://web.archive.org/web/20250326021354/https://www.informit.com/articles/article.aspx?p=23416 (verified by fetch with curl; title "Interview with Bruce Eckel", Sep 21, 2001). The link text on the media page also has a typo: "InforIT".
- **Thinking in Java Interview (June 2001)**, `javaworld.com/article/2076009/core-java/eckel-thinks-in-java.html`: redirects to the InfoWorld home page. Replacement: https://www.infoworld.com/article/2161387/eckel-thinks-in-java.html (verified by fetch; "Eckel thinks in Java", John Zukowski, June 8, 2001). A Wayback copy of the JavaWorld original also exists: http://web.archive.org/web/20170628180857/http://www.javaworld.com:80/article/2076009/core-java/eckel-thinks-in-java.html (verified by fetch with curl).

Blocked to automated clients (403), probably fine in a browser:

- **Java Magazine Articles**, https://blogs.oracle.com/authors/bruce-eckel: 403 to curl and to the fetch tool. A Wayback snapshot from March 10, 2026 shows the author page still existed then (http://web.archive.org/web/20260310125409/https://blogs.oracle.com/authors/bruce-eckel/, verified by fetch with curl), though its article list did not render without JavaScript. Check in a browser.
- **Java Magazine review of On Java 8 (Sept 2017)**, https://blogs.oracle.com/javamagazine/post/book-review-on-java-8-eckel: 403. A Wayback snapshot from August 7, 2025 exists (http://web.archive.org/web/20250807043504/https://blogs.oracle.com/javamagazine/post/book-review-on-java-8-eckel, availability confirmed through the Wayback API; body not readable). Check in a browser.

Working, but redirecting to a new address worth updating:

- **Interview with Eric Gunnerson (Feb 2004)**, `blogs.msdn.microsoft.com/ericgu/2004/02/09/insights-into-the-net-architecture/` now redirects to https://learn.microsoft.com/en-us/archive/blogs/ericgu/insights-into-the-net-architecture (status 200 only).
- **Rethinking Scala (May 2014)**, the SlideShare link now redirects to https://www.slideshare.net/slideshow/rethinking-scala-presented-in-san-francisco-may-7-2014/34401420 (status 200 only).
- **PyDev of the Week (Nov 2017)**, `www.blog.pythonlibrary.org/...` now redirects to https://blog.pythonlibrary.org/2017/11/06/pydev-of-the-week-bruce-eckel/ (status 200 only).

Returning 200 at the listed address (status 200 only; content not read):
happypathprogramming.com; the five `youtu.be` links and four `youtube.com/watch` links; the WeChat InfoQ China article (`mp.weixin.qq.com`; WeChat often shows a verification page to non-browser clients, so check in a browser); realpython.com podcast 116; the Geecon 2019 Google Slides link; talkpython.fm episode 148; opensource.com interview; cds.cern.ch record 1390426; both infoq.com news items (each adds a trailing slash); both javaposse.com pages; artima.com/articles/python-and-the-programmer.

### Inferences
- InformIT appears to have retired its old `article.aspx?p=` article pages sometime after mid-2025, since Wayback has good snapshots from March and May 2025 and the live URLs now return the index.
- YouTube returns 200 for removed videos too, so a 200 on those nine links does not prove the videos are still up. A browser check is the reliable test.

### Gaps
- No replacement was found for the VJug24 keynote link.
- The Vimeo and OSCON replacement candidates are unconfirmed, as noted.
- The media page labels the opensource.com piece "June 2015 O'Reilly Interview" while its URL path says July 2015 (`/life/15/7/`); I did not fetch the page to settle the month.
