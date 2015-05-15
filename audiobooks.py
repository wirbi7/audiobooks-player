from gi.repository import Gtk, Gst, GObject
import sys

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def on_button_clicked(self, button):
        print("Hello World!")
        pipeline = Gst.Pipeline(name='note')
        source = Gst.ElementFactory.make('audiotestsrc', 'src')
        sink = Gst.ElementFactory.make('autoaudiosink', 'output')

        source.set_property('freq', 329.63)
        pipeline.add(source)
        pipeline.add(sink)
        source.link(sink)
        pipeline.set_state(Gst.State.PLAYING)

        GObject.timeout_add(5000, self.pipeline_stop, pipeline)
        #pipeline.set_state(Gst.State.NULL)
        entry = builder.get_object('entry1')
        entry.set_text('звук пошел')

    def pipeline_stop(self, pipeline):
        pipeline.set_state(Gst.State.NULL)
        return False

Gst.init_check(sys.argv)
builder = Gtk.Builder()
builder.add_from_file("audiobooks.glade")
builder.connect_signals(Handler())

liststore1 = builder.get_object('liststore1')
liststore1.append({'1 скок поскок'})

liststore2 = builder.get_object('liststore2')
liststore2.append({'1.mp3'})
liststore2.append({'2.mp3'})
liststore2.append({'3.mp3'})
liststore2.append({'4.mp3'})
liststore2.append({'5.mp3'})
liststore2.append({'6.mp3'})
liststore2.append({'7.mp3'})
liststore2.append({'8.mp3'})
liststore2.append({'9.mp3'})
liststore2.append({'10.mp3'})
liststore2.append({'11.mp3'})
liststore2.append({'12.mp3'})

window = builder.get_object("window1")
window.show_all()

Gtk.main()