import pytest

from needle.updates.cellar_feed import FeedParseError, parse_feed


def test_malformed_notification_is_not_silently_dropped():
    rss = b'''<rss><channel><item>
      <id>42</id><cellarId>cellar:x</cellarId><rootCellarId>cellar:r</rootCellarId>
      <type>UPDATE</type>
    </item></channel></rss>'''
    with pytest.raises(FeedParseError, match="ingestion_time"):
        parse_feed(rss)


def test_unknown_action_blocks_window_instead_of_becoming_event():
    rss = b'''<rss><channel><item>
      <id>42</id><cellarId>cellar:x</cellarId><rootCellarId>cellar:r</rootCellarId>
      <type>REWRITE</type><date>2026-09-20T10:00:00+00:00</date>
    </item></channel></rss>'''
    with pytest.raises(FeedParseError, match="unknown action"):
        parse_feed(rss)


def test_unknown_xml_root_is_not_misclassified_as_atom():
    with pytest.raises(FeedParseError, match="unsupported feed root"):
        parse_feed(b"<notifications />")
