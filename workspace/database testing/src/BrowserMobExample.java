import java.io.File;
import java.io.IOException;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Proxy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;


import net.lightbody.bmp.BrowserMobProxy;
import net.lightbody.bmp.proxy.ProxyServer;
import net.lightbody.bmp.BrowserMobProxyServer;
import net.lightbody.bmp.client.ClientUtil;
import net.lightbody.bmp.core.har.Har;
import net.lightbody.bmp.proxy.CaptureType;

public class BrowserMobExample {
	
	
	String sFileName = "C:/tmp/open.har";
	
	public WebDriver driver;
	public BrowserMobProxy proxy;
	
	@Before
	public void setUp() {
		
	   // start the proxy
	    proxy = new BrowserMobProxyServer();
	    proxy.start(0);

	    //get the Selenium proxy object - org.openqa.sele
	    Proxy seleniumProxy = ClientUtil.createSeleniumProxy(proxy);

	    // configure it as a desired capability
	    DesiredCapabilities capabilities = new DesiredCapabilities();
	    capabilities.setCapability(CapabilityType.PROXY, seleniumProxy);
		
	    //set chromedriver system property
		
		driver = new ChromeDriver(capabilities);
		
	    // enable more detailed HAR capture, if desired (see CaptureType for the complete list)
	    proxy.enableHarCaptureTypes(CaptureType.REQUEST_HEADERS,CaptureType.REQUEST_CONTENT, CaptureType.RESPONSE_HEADERS,CaptureType.RESPONSE_CONTENT);

	    // create a new HAR with the label "seleniumeasy.com"
	    proxy.newHar("openagent.com.au");

	    // open seleniumeasy.com
	    driver.get("http://www.openagent.com.au");
        
	}
	
	@Test
	public void testCaseOne() {
		System.out.println("Navigate to selenium tutorials page");
		driver.findElement(By.id("f_suburb")).click();
	}
	
	@After
	public void tearDown() {

		// get the HAR data
		Har har = proxy.getHar();

		// Write HAR Data in a File
		File harFile = new File(sFileName);
		try {
			har.writeTo(harFile);
		} catch (IOException ex) {
			 System.out.println (ex.toString());
		     System.out.println("Could not find file " + sFileName);
		}
		
		if (driver != null) {
			proxy.stop();
			driver.quit();
		}
	}
}