from selenium import selenium
import unittest, time, re

class TextControlTests(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*custom firefox -p selenium -no-remote", "http://localhost:8080/")
        #self.selenium = selenium("localhost", 4444, "*opera", "http://localhost:8080/")
        self.selenium.start()

    def test_simple(self):
        sel = self.selenium
        current_time = "%.0f" % time.time()

        sel.open("/testingyui/")
        sel.click("link=Create new Thing")
        sel.wait_for_page_to_load("30000")
        name = "Simple Thing [%s]" %current_time
        description = "This is a simple thing. Created at: %s" % current_time
        sel.type("name", name)
        sel.type("description", description)
        sel.click("Save")
        sel.wait_for_page_to_load("30000")
        sel.click(name)
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present(name))
        self.failUnless(sel.is_text_present(description))
        
    def test_nic(self):
        sel = self.selenium
        current_time = "%.0f" % (time.time() * 10000)

        sel.open("/testingyui/")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Nic Editor")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Create new Thing")
        sel.wait_for_page_to_load("30000")
        
        # give the editor a second to load
        time.sleep(1)
        name = "Nic Thing [%s]" %current_time
        description = "This is a nic thing - Created at: %s" % current_time
        sel.type("name", name)
        
        editor_locator = "//div[@id='html_entry']/div[2]/div"        
        sel.focus(editor_locator)
        
        # BUG: Note that dot (.) cannot be entered using this method. This is a bug in selenium.
        # http://jira.openqa.org/browse/SEL-519
        sel.type_keys(editor_locator, description)        
        sel.click("Save")
        sel.wait_for_page_to_load("30000")
        sel.click(name)
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present(name))
        self.failUnless(sel.is_text_present(description))

    def test_yui(self):
        sel = self.selenium
        current_time = "%.0f" % time.time()

        sel.open("/testingyui/")
        sel.wait_for_page_to_load("30000")
        sel.click("link=YUI Editor")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Create new Thing")
        sel.wait_for_page_to_load("30000")
        
        # give the editor a second to load
        time.sleep(1)
        name = "YUI Thing [%s]" %current_time
        description = "This is a yui thing. Created at: %s" % current_time
        sel.type("name", name)
        
        html_data = "<body>" + description + "</body>"
        sel.run_script("myEditor.setEditorHTML(" + html_data + ");")
        
        sel.click("Save")
        sel.wait_for_page_to_load("30000")
        sel.click(name)
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present(name))
        self.failUnless(sel.is_text_present(description))
 
    def test_fck(self):
        sel = self.selenium
        current_time = "%.0f" % time.time()

        sel.open("/testingyui/")
        sel.wait_for_page_to_load("30000")
        sel.click("link=FCK Editor")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Create new Thing")
        sel.wait_for_page_to_load("30000")
        
        # give the editor a second to load
        time.sleep(1)
        name = "FCK Thing [%s]" %current_time
        description = "This is a fck thing. Created at: %s" % current_time
        sel.type("name", name)
        
        html_data = "<body>" + description + "</body>"
        sel.run_script("var oEditor = FCKeditorAPI.GetInstance('description'); oEditor.SetHTML(" + html_data + ");")
        
        sel.click("Save")
        sel.wait_for_page_to_load("30000")
        sel.click(name)
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present(name))
        self.failUnless(sel.is_text_present(description))
   
    def tearDown(self):
        self.selenium.stop()



if __name__ == "__main__":
    unittest.main()
