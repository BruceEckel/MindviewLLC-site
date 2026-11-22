# Bruce Eckel: Internet Archive check of dead, unverified, and missing media items

Research date: 2026-11-22.
Method: Wayback CDX and availability APIs queried with curl, snapshots fetched as raw HTML (`/web/<timestamp>id_/<url>`), and the archive.org advanced-search and metadata APIs.
The Archive went "Temporarily Offline" intermittently during the session; every lookup below that depends on a snapshot was repeated until it returned real content.

Status labels:
- **verified**: snapshot fetched and content matches.
- **snapshot exists but content not confirmed**: a capture is listed, but the body is a JavaScript shell, a pointer, or a 404.
- **nothing found**.

Sources checked first: `C:\git\MindviewLLC-site\content\media\index.md` and the four notes in this folder.

## Summary table

| # | Item | Result | Best URL |
|---|---|---|---|
| 1 | VJUG24 keynote, "An Overview of Kotlin for Java Programmers" | Wayback: nothing found (captures of the URL are all 404). YouTube recording found and verified | https://www.youtube.com/watch?v=lU_WJGhvoDs |
| 2 | OSCON 2015 "Creating Trust Organizations" | verified | http://web.archive.org/web/20191120193433/https://conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/41505 |
| 3a | Oracle Java Magazine author page | snapshot exists but content not confirmed (JavaScript shell) | http://web.archive.org/web/20260310125409/https://blogs.oracle.com/authors/bruce-eckel/ |
| 3b | Java Magazine review of On Java 8 | snapshot exists but content not confirmed (JavaScript shell) | http://web.archive.org/web/20240304225055/https://blogs.oracle.com/javamagazine/post/book-review-on-java-8-eckel |
| 3c | Eckel Index (July 1, 2022) and his seven 2022 articles | index verified; 3 of 7 article pages verified; titles and dates of all 7 verified from Wayback copies of the Java Magazine RSS feed | http://web.archive.org/web/20240104173544/https://blogs.oracle.com/javamagazine/post/java-eckel-index |
| 4 | Heroku talk, May 2012 (Vimeo) | nothing found (Wayback has only a 301 then 404; live Vimeo page is an unlabeled shell) | none |
| 5 | The Flex Show episode 50 (Aug 13, 2008) | verified (page text); audio file not archived | http://web.archive.org/web/20080823221848/http://www.theflexshow.com:80/blog/index.cfm/2008/8/13/The-Flex-Show-Episode-50-Interview-James-Ward-and-Bruce-Eckell |
| 6 | EuroPython 2009 keynotes (blip.tv) | blip.tv pages verified as "bruce-eckel-keynote.1" and ".2"; the video files are not archived and no other mirror found | http://web.archive.org/web/20090717070031/http://europython09.blip.tv:80/file/2338437 |
| 7 | UC Berkeley Haas June 2004 RealMedia stream | snapshot exists but content not confirmed (75-byte pointer file only; the stream itself is not archived) | http://web.archive.org/web/20070614045731/http://video.haas.berkeley.edu:24874/ramgen/media-services/Eckel6-25-04.rm |
| 8 | Borland interview by Clay Shannon | verified; dated July 15, 2003 (conducted by email, June 2003) | http://web.archive.org/web/20080517031942/http://community.borland.com/article/0,1410,30139,00.html |
| 9 | Other dead links in the notes | informit x2, javaworld, typesafe re-verified; Stitcher nothing found; Dr. Dobb's Jolt page has Wayback captures (not fetched) | see Part A, item 9 |
| B | archive.org collections | 2 relevant videos (Open Spaces intro, two copies), Thinking in C seminar, two Hands-On Java CDs | see Part B |

Findings outside the Internet Archive that this check turned up, none of them in the media page or the four notes: four more YouTube recordings (see "New recordings found", below).

## Part A: Wayback Machine replacements

### 1. VJUG24 keynote, November 2017

Media page entry: `https://virtualjug.com/vjug24-keynote-an-overview-of-kotlin-for-java-programmers/`.

- Wayback: **nothing found.** The CDX API lists about 80 captures of that URL from 2018-03-07 to 2019, and every one is a 404 or an unrecorded status. No capture earlier than March 2018 exists. The vJUG home page snapshots from January and February 2018 (`web/20180122031402` and `web/20180228223254`) do not mention Eckel or the Kotlin talk. The 2017 vJUG24 pages that do exist (for example `https://virtualjug.com/vjug24-keynote-the-art-of-simplicity/`, captured 2017-10-03) are other sessions.
- **YouTube recording, verified (oEmbed plus watch-page metadata):** title "vJUG24: 17/24 An Overview of Kotlin for Java Programmers", channel "v JUG" (`https://www.youtube.com/@virtualJUG`), uploaded 2017-11-02. The description says the talk draws on examples from the upcoming Atomic Kotlin book and names Bruce Eckel as speaker. URL: https://www.youtube.com/watch?v=lU_WJGhvoDs
- **Event page, verified from a Wayback copy:** the Bulgarian JUG listing "Beer, Pizza & vJUG24 2017" (Questers, Sofia) lists "KEYNOTE: An Overview of Kotlin for Java Programmers (Bruce Eckel)" in the local 02:00 to 03:00 slot and dates the event 25 October 2017. Snapshot: http://web.archive.org/web/20191113065310/https://www.questers.com/events/beer-pizza-vjug24-2017 (the live address now redirects to pwrteams.com).
- **Date conflict:** the media page says November 2017. The talk was part of the 24-hour vJUG24 held on 25 October 2017; the YouTube upload is 2 November 2017. "October 2017" is the date of the talk, so the page entry is probably wrong by a month.

### 2. OSCON 2015 "Creating Trust Organizations"

Result: **verified.** Snapshot: http://web.archive.org/web/20191120193433/https://conferences.oreilly.com/oscon/open-source-2015/public/schedule/detail/41505

The fetched page title is "Creating trust organizations: O'Reilly Open Source Convention: OSCON, July 20 - 24, 2015 in Portland, OR". Page text: "Bruce Eckel (Mindview, LLC)", 2:30pm to 3:10pm Wednesday, 07/22/2015, Collaboration, room D137/138, average rating 3.43 (7 ratings), a "Slides: 1-PDF" link, and the abstract about the "Trust Organization Manifesto". The talk date is **July 22, 2015**, not June 2015 as the media page says (the conference ran July 20 to 24).
Other captures of the same URL exist for 2016-03-11, 2016-04-28, 2019-08-22, and 2019-09-17 (`web/<timestamp>/` plus the URL).

### 3. Oracle Java Magazine

**3a. Author page** `https://blogs.oracle.com/authors/bruce-eckel`: snapshot exists but content not confirmed. CDX lists 200 captures from 2024-01-04 to 2026-03-10. Every body is a JavaScript shell ("This site requires JavaScript to be enabled"), so no article list is readable. Snapshot: http://web.archive.org/web/20260310125409/https://blogs.oracle.com/authors/bruce-eckel/

**3b. Review of On Java 8** `https://blogs.oracle.com/javamagazine/post/book-review-on-java-8-eckel`: snapshot exists but content not confirmed. Captures run from 2022-08-16 to 2025; all bodies are the same JavaScript shell, and no title, author, or date is readable. A web search for the review returned nothing. Snapshot: http://web.archive.org/web/20240304225055/https://blogs.oracle.com/javamagazine/post/book-review-on-java-8-eckel

**3c. Eckel Index and the seven 2022 articles.**

- Index page, **verified**: http://web.archive.org/web/20240104173544/https://blogs.oracle.com/javamagazine/post/java-eckel-index. Title "The Eckel Index: New language features from Java 9 through Java 17", July 1, 2022, by Alan Zeichick (editor in chief). It states "Earlier in 2022, Java Magazine published seven articles by Bruce Eckel (author of On Java 8 version 2)" and lists each article's topics. The page links the seven articles by URL.
- Titles and dates: the page titles of articles 5, 6, and 7 were read from fetched snapshots. All seven titles and dates come from Wayback copies of the Java Magazine RSS feed (`https://blogs.oracle.com/javamagazine/rss`, captures of 2022-08-18 and 2023-05-28). The article pages for #1 to #4 have only JavaScript-shell snapshots.

| # | Title | Date | URL | Status |
|---|---|---|---|---|
| 1 | Bruce Eckel on simplifying local variable type inference in Java | 2022-03-21 (RSS) | https://blogs.oracle.com/javamagazine/post/java-local-reference-type-inference | title and date from RSS; page is a shell |
| 2 | Bruce Eckel on Java records | 2022-04-07 (RSS) | https://blogs.oracle.com/javamagazine/post/java-records-constructor-methods-inheritance | title and date from RSS; page is a shell |
| 3 | Bruce Eckel on Java interfaces and sealed classes | 2022-04-25 (RSS) | https://blogs.oracle.com/javamagazine/post/java-interface-sealed-class | title and date from RSS; page is a shell |
| 4 | Bruce Eckel on switch expressions, arrow syntax, and case null | 2022-05-06 (RSS) | https://blogs.oracle.com/javamagazine/post/java-switch-expression-arrow-case-null | title and date from RSS; page is a shell |
| 5 | Bruce Eckel on pattern matching in Java | May 20, 2022 (page, 10 minute read) | https://blogs.oracle.com/javamagazine/post/java-pattern-matching | verified: http://web.archive.org/web/20240104173545/https://blogs.oracle.com/javamagazine/post/java-pattern-matching |
| 6 | Bruce Eckel on Java pattern matching guards and dominance | June 3, 2022 (page, 8 minute read) | https://blogs.oracle.com/javamagazine/post/java-pattern-matching-guards-coverage-dominance | verified: http://web.archive.org/web/20240104173545/https://blogs.oracle.com/javamagazine/post/java-pattern-matching-guards-coverage-dominance |
| 7 | Bruce Eckel on Java modules, text blocks, and more | June 16, 2022 (page, 9 minute read) | https://blogs.oracle.com/javamagazine/post/java-modules-textblocks-trywithresources-nullpointerexception | verified: http://web.archive.org/web/20240104173616/https://blogs.oracle.com/javamagazine/post/java-modules-textblocks-trywithresources-nullpointerexception |

The index's own wording for the article subjects: #1 "Simplifying local variable type inference", #2 "Java records", #3 "Interfaces and sealed classes", #4 "Switch expressions, arrow syntax, and case null", #5 "Pattern matching", #6 "Pattern matching guards and dominance", #7 "Java modules, text blocks, and more".
The RSS dates for #1 to #4 are feed timestamps; the pages' own bylines for those four could not be read, so a one-day difference from the displayed date is possible.
The fetched pages for #5 to #7 show the same dates as the RSS feed (May 20, June 3, June 16).

### 4. Heroku talk, May 2012

- `https://vimeo.com/herokai/review/40551380/dbcaffb1e2`: **nothing found.** CDX has a single capture (2016-08-05) with status 301, and following it in the Wayback gives a 404.
- `https://vimeo.com/40551380`: no Wayback captures. The live URL returns HTTP 200, but the body is a `noindex` shell with no title, and Vimeo's oEmbed endpoint answers 404 for it. Title and owner **cannot be confirmed**; the video is probably private or removed. The earlier note's "returns 200" is true but means nothing here.
- No other copy of a Heroku talk by him turned up. A YouTube search found a different recording of "Reinventing Business" (see "New recordings found").

### 5. The Flex Show episode 50

Result: **verified (page text).** Snapshot: http://web.archive.org/web/20080823221848/http://www.theflexshow.com:80/blog/index.cfm/2008/8/13/The-Flex-Show-Episode-50-Interview-James-Ward-and-Bruce-Eckell

The fetched page reads "The Flex Show Episode 50: Interview James Ward and Bruce Eckel", posted August 13, 2008 by Jeffry Houser. Text: "Jeff and I got a chance to catch up with James Ward, Technical Evangelist for Adobe and Bruce Eckel, Consultant to Adobe, together working on their new book. They talk (we listen) about Flex, Java, RIAs in general." The show notes list JavaFX, Java Swing, Blaze DS, Mate Framework, The Java Posse, Silverlight, and links to both blogs. Three comments follow (one by Jeffry Houser).
The hosts are Jeffry Houser and John Wilker ("Contact E-mail Jeffry and John"; the page names Houser as poster).

Other good captures: 2008-08-30, 2008-08-31, 2008-09-03, 2008-11-21, 2009-11-26, 2016-04-15, 2016-10-13.
The earlier note's 2024-11-23 snapshot was the near-empty one; the 2008 captures are the full page.
The audio link is `http://www.theflexshow.com/blog/download.cfm/id/B885DACC-2BF4-55D0-F64A3B7FFE06F86C/TheFlexShow_Episode50.mp3`. The 2016 captures of it are redirects (302) to an `enclosures/...mp3` address that the Wayback returns 404 for, so the audio itself is **nothing found**.

### 6. EuroPython 2009 keynotes (blip.tv)

The two blip.tv pages that Michael Sparks's July 13, 2009 list names are in the Wayback, **verified as pages**:

- http://web.archive.org/web/20090717070031/http://europython09.blip.tv:80/file/2338437 : page title "bruce-eckel-keynote.1"; show "europython09"; the file would be `http://blip.tv/file/get/Kamaelian-bruceeckelkeynote1501.flv`.
- http://web.archive.org/web/20090717070021/http://europython09.blip.tv:80/file/2338433 : page title "bruce-eckel-keynote.2"; file `http://blip.tv/file/get/Kamaelian-bruceeckelkeynote2394.flv`.

Both captures confirm that the recordings were Eckel's keynote, split in two parts. Neither page gives a talk title or description.
**The video files are not archived:** CDX has no captures for either `.flv` address, and an archive.org search for "europython 2009 eckel" returns nothing.
Other mirrors: pyvideo.org has no EuroPython 2009 event page (404), and its Eckel speaker page lists only the PyCaribbean 2017 keynote, PyCon US 2013, 2022, 2023, and 2024. A YouTube search for the 2009 keynote returned nothing. Result for the recordings: **nothing found.**
Related and already in the other notes: the 2010 list post "Europython videos all now posted up" (https://mail.python.org/pipermail/europython/2010-August/007818.html) was fetched and does not mention Eckel.

### 7. UC Berkeley Haas, June 25, 2004 "Java Issues & Directions"

- OSNews post, **verified:** http://web.archive.org/web/20190918195426/https://www.osnews.com/story/7646/a-talk-by-bruce-eckel-java-issues-directions/ . Text: "A Talk by Bruce Eckel: Java Issues & Directions", submitted by TTF 2004-07-11, "at UC Berkeley, Haas School of Business on 25-Jun-2004", with a "Link for Real streaming video here" pointing to the `.rm` address below. Comments (37) include one reporting the stream would not download.
- Stream pointer, **snapshot exists but content not confirmed:** http://web.archive.org/web/20070614045731/http://video.haas.berkeley.edu:24874/ramgen/media-services/Eckel6-25-04.rm (content type `audio/x-pn-realaudio`, 75 bytes). The content is only the text `rtsp://128.32.75.11:554/media-services/Eckel6-25-04.rm?cloakport=8080,554`. That is a RealMedia pointer to a streaming server, not the media, and the Wayback cannot capture RTSP, so the recording is **nothing found.**
- His own post, **verified:** http://web.archive.org/web/20040712034604/http://mindview.net:80/WebLog/log-0055 , "7-9-04 Java Issues & Directions": "On June 25, 2004 at the UC Berkeley Haas School of Business, I gave a presentation for the California Digital Library on issues and directions for the Java language... The presentation is 2 hours 16 minutes long." It also says the feed is hosted on the Berkeley server and needs a RealMedia player. This gives the sponsor (California Digital Library) and length, which no earlier note has.
- Dion Almaer's post is also archived: http://web.archive.org/web/20071020194926/http://almaer.com/blog/bruce-eckel-video-talking-about-java (captured, not read).

### 8. Borland Developer Network interview by Clay Shannon

Result: **verified.** Two snapshots fetched:

- http://web.archive.org/web/20080517031942/http://community.borland.com/article/0,1410,30139,00.html (the one named in the task): page title "Interview with Bruce Eckel by Clay Shannon", full interview text.
- http://web.archive.org/web/20030718042625/http://community.borland.com:80/article/0,1410,30139,00.html (earliest capture, with the original Borland page chrome).

The abstract reads "OOP guru Bruce Eckel talks about his initial skepticism about C# (but now calls it 'a better Java'), wishes Borland would create a Python IDE, explains why he's suspicious of Mono, and asks us to click the wombat."
**Date:** the page footer says "Article ID: 30139 Publish Date: July 15, 2003 Last Modified: July 15, 2003", and the closing note says "This interview was conducted via email June 2003." This answers the gap in `written_interviews_and_articles.md`.

### 9. Other dead or search-results-only URLs in the four notes

| Item | Result |
|---|---|
| InformIT "Interview with Bruce Eckel" (Sep 21, 2001) | verified again: http://web.archive.org/web/20250326021354/https://www.informit.com/articles/article.aspx?p=23416 |
| InformIT "Is This the Best We Can Do? A Conversation with Bruce Eckel, Part I" (May 18, 2007) | verified again: http://web.archive.org/web/20250513191100/https://www.informit.com/articles/article.aspx?p=762675 |
| JavaWorld "Eckel thinks in Java" (June 2001) | verified again: http://web.archive.org/web/20170628180857/http://www.javaworld.com:80/article/2076009/core-java/eckel-thinks-in-java.html |
| Typesafe blog, "Bruce Eckel on Learning Scala and Tech Conferences" (July 2013) | verified again (page title matches): http://web.archive.org/web/20150907021510/https://www.typesafe.com/blog/bruce-eckel-on-learning-scala-and-tech-conferences |
| Stitcher Frontmatter episode URL | nothing found: CDX has no 200 capture. The Leanpub page named in the notes remains the replacement. |
| Dr. Dobb's Jolt Awards page (June 2003) | snapshot exists but content not confirmed (not fetched here): CDX lists 200 captures of `http://www.drdobbs.com/joltawards/the-13th-annual-software-development-jol/184414991` on 2012-10-07, 2013-01-15, and 2013-04-06. The earlier note says it read a Wayback copy. |
| Artima "Python and the Tipping Point" (`artima.com/intv/tipping.html`) | snapshot exists but content not confirmed (not fetched): 200 captures from 2003-07-25. |
| VuWall YouTube link `6DYLJGwrTo0` | not an Internet Archive question; unchanged. |

## Part B: items in the Internet Archive's own collections

Searches run through the advanced-search API: `"Bruce Eckel"` (29 hits), `"Eckel, Bruce"`, creator, subject, and description variants, with and without `mediatype:movies`, `mediatype:audio`, `mediatype:data`, and `mediatype:software`, plus "MindView", "Thinking in C", "Hands-On Java", "Java Posse", "IT Conversations", "Dr. Dobb", "World of C++", Borland, and the titles of each of his later books.
Searches for "Java Posse", "IT Conversations", "Dr. Dobb", Borland "World of C++" videos, "Atomic Kotlin", "Atomic Scala", and "Reinventing Business" returned **nothing** that involves him.
The `mediatype:audio` search for him returns one item, which only tags him (below). Plain scans of his books and items about a different Eckel (Tim, Mike, Wendy Sand, Nathan, and others) are excluded.

### Relevant items

| Title | Date | Mediatype | URL | In media page or notes? |
|---|---|---|---|---|
| Open Spaces by Bruce Eckel | uploaded 2009-01-09 | movies | https://archive.org/details/OpenSpacesByBruceEckel | **No** |
| Introduction to Open Spaces | uploaded 2009-01-09 | movies | https://archive.org/details/BruceEckelIntroductiontoOpenSpaces | **No** |
| Thinking In C (multimedia seminar by Chuck Allison for MindView) | uploaded 2018-01-11 | texts (a zip of the Flash seminar) | https://archive.org/details/ThinkingInC | **No** |
| Thinking in C: Foundations for Java & C++ (Beta), Chuck Allison & MindView Inc. | uploaded 2006-03-17 | data | https://archive.org/details/ChuckAllisonMindViewInc | **No** |
| Thinking in C: Foundations for Java and C++, Chuck Allison & Bruce Eckel | uploaded 2006-03-27 | data | https://archive.org/details/ChuckAllisonBruceEckel_4 | **No** |
| Bruce Eckels Hands On Java 1st Ed (CD-ROM image, "(c) 1998 MindView, Inc") | uploaded 2024-05-21 | software | https://archive.org/details/bruce-eckels-hands-on-java-1st-ed | **No** |
| Bruce Eckels Hands On Java 2nd Ed (companion CD image) | uploaded 2024-05-22 | software | https://archive.org/details/bruce-eckels-hands-on-java-2nd-ed | **No** |

Details, each read from the item's metadata:

- **Open Spaces videos (two uploads of one recording).** Both are by uploader `tshanky@gmail.com` and have the description "Introduction to Open Spaces". Each has an `.ogv`, `.mov`, and 512 kb `.mp4` derivative of 477.2 seconds (7 minutes 57 seconds). The first sits in `opensource_movies`; the second, which carries a Creative Commons Attribution 2.5 license, sits in `ourmedia`. The upload date matches the YouTube upload "Open Spaces Introduction (by Bruce Eckel)" by Douglas Napoleone (2009-01-09) that `podcasts_and_video_interviews.md` lists as a talk missing from the media page, so this is probably the same recording. The Archive copies add a stable, downloadable home for it. The recording's event is not stated (the notes' QCon SF 2008 "Evening Open Space Introduction" is a possible match but is unconfirmed).
- **Thinking in C.** The `ThinkingInC` item (97.9 MB zip, license CC BY-NC-ND 3.0, uploaded by `mindviewinc@gmail.com`) describes "the Thinking in C multimedia seminar (created for MindView by Chuck Allison)". The two 2006 `data` items hold the Flash-based seminar as `ThinkingInCBeta.zip` (167.8 MB), uploaded by `lists.eckel@gmail.com`. This is the "Thinking in C" CD content named in the brief.
- **Hands-On Java CDs.** Both are ISO images (about 422 MB and 510 MB) in the `cdrom_contributions` collection, uploaded in May 2024 by `chisarickd@doombridge.com`. The brief's "Hands-On Java CD content" is these. Whether the CDs hold recorded lectures was not checked; only the metadata was read.
- **Others in the first search**, not media and so not listed above: scans of Thinking in Java (several editions), Thinking in C++ (volumes 1 and 2), Thinking in Patterns, Piensa en Java, "Black Belt C++", "Using C++", "C++ Inside & Out", "First steps in Flex" (Eckel and Ward, 2008, a borrowable scan), and GitHub archive snapshots of the On Java 8 repository by the user LingCoder.
- **Tag-only mention, not an appearance:** `castalio-podcast-35` ("Castalio Podcast, Fabio Kung e Pedro Belo: Heroku", 2012-04-29, audio, https://archive.org/details/castalio-podcast-35) lists "bruce eckel" among about 60 subject tags. The description does not name him, so he is probably a topic raised in conversation, not a guest. It is a Portuguese-language Heroku episode from the same month as his Heroku talk, which is why it surfaced. Treat as not relevant unless someone listens to it.
- **Software CD:** `CMCD1001` (CHIP CD-ROM Romania, October 2001) mentions him in its description, apparently because the disc carries an electronic edition of a book. Not media; excluded.

## New recordings found (outside the Internet Archive; not in the media page or the four notes)

The YouTube searches run to find the vJUG video returned these Eckel recordings. Each was checked with YouTube's oEmbed endpoint and the watch page.

| Title | Channel | Date | URL | Note |
|---|---|---|---|---|
| vJUG24: 17/24 An Overview of Kotlin for Java Programmers | v JUG | uploaded 2017-11-02 | https://www.youtube.com/watch?v=lU_WJGhvoDs | The dead VJUG24 item (Part A, item 1) |
| GeeCON 2019: Bruce Eckel - Three Programming Disruptions | geecon conference | uploaded 2019-07-24 | https://www.youtube.com/watch?v=K5EFqfnx-0I | Recording for the GeeCON 2019 talk; `other_conference_talks.md` found no video |
| Reinventing Business (Bruce Eckel) | javaposse | uploaded 2011-03-05 | https://www.youtube.com/watch?v=yyyfvG-jjko | Description: "Java Posse Roundup 2011 Lightning Talk... Recorded in Crested Butte, CO on Feb 22, 2011" |
| OSCON 2013: Reinventing Business - Bruce Eckel | O'Reilly | uploaded 2014-02-19 | https://www.youtube.com/watch?v=gt5OSmJfQL0 | Full OSCON 2013 talk; the media page has only the OSCON 2013 interview (`ZPGboUNisOg`) |
| Bruce Eckel comparing features in Java 17 and Kotlin | Java and Kotlin user group | uploaded 2021-11-01 | https://www.youtube.com/watch?v=xU-gbzcToOs | Talk title and event not read; description starts "To steal Bruce's words" |
| Pyconbrasil2008 - Why I love Python - Bruce Eckel - Sat - 18-09-2008 | Giuseppe Romagnoli | uploaded 2012-05-23 | https://www.youtube.com/watch?v=3OTMR-H2IUI | Video for the PyConBrasil 2008 talk; `python_talks.md` lists the talk but this video id appears in none of the notes |
| Bruce Eckel - Keynote | PyCaribbean | uploaded 2017-03-20 | https://www.youtube.com/watch?v=_ncc69-cunA | PyCaribbean 2017 keynote; the python notes cover the talk through pyvideo |

Title, channel, and upload date were read for all seven; no video was watched, so the talk content is taken from the titles and descriptions.

## Gaps

- Oracle's Java Magazine pages (author page, the On Java 8 review, and articles 1 to 4) have only JavaScript-shell snapshots. A browser is the only way to read the review's title, date, and author.
- The Haas 2004 stream, both EuroPython 2009 keynote video files, the Flex Show audio, and the 2012 Heroku talk have no surviving copy that this check found.
- The Archive search covers metadata only; full-text search of scanned items (for example Dr. Dobb's Journal or Micro Cornucopia scans naming him) was not run.
- Wayback snapshots of the `javaposse.com` episode pages and of the Java Posse Roundup session recordings were not searched.

## Suggested follow-ups

- Update the media page entries in place: the VJUG24 link to the YouTube address above (and the date to October 2017), the OSCON 2015 link to the Wayback address above (and the date to July 2015), and the Flex Show and Borland items to the Wayback addresses.
- The notes disagree with these findings in two places: `written_interviews_and_articles.md` says no VJUG24 replacement exists, and its OSCON entry is marked "content unconfirmed".
