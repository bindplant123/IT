Practical No : 01  
 
AIM : Android Resources: (Color, Theme, String, Drawable, Dimension, Image) Project Structure  
res/ 
 ├── values/ 
 │    ├── colors.xml 
 │    ├── strings.xml 
 │    ├── dimens.xml 
 │    └── themes.xml 
 │ 
 ├── drawable/ 
 │    └── rounded_bg.xml 
 │ 
 ├── layout/ 
 │    └── activity_main.xml 
 │ 
 └── mipmap/ 
      └── ic_launcher.png   (default app image) 
 
1. colors.xml (Color Resource)  res/values/colors.xml 
<resources> 
    <color name="purple_500">#6200EE</color> 
    <color name="purple_700">#3700B3</color> 
    <color name="teal_200">#03DAC5</color> 
    <color name="white">#FFFFFF</color> 
    <color name="black">#000000</color> 
</resources> 
 
2. strings.xml (String Resource) res/values/strings.xml 
<resources> 
    <string name="app_name">Resource Demo</string> 
    <string name="welcome_text">Welcome to Android Resources</string> 
    <string name="click_me">Click Me</string> </resources> 
3. dimens.xml (Dimension Resource) res/values/dimens.xml 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
<resources> 
    <dimen name="text_size">18sp</dimen> 
    <dimen name="padding">16dp</dimen> 
    <dimen name="button_height">50dp</dimen> 
</resources> 
 
 4. themes.xml (Theme Resource)  res/values/themes.xml 
<resources xmlns:tools="http://schemas.android.com/tools"> 
 
    <style name="Theme.ResourceDemo" 
parent="Theme.Material3.DayNight.NoActionBar"> 
        <item name="colorPrimary">@color/purple_500</item> 
        <item name="colorPrimaryVariant">@color/purple_700</item>         <item name="colorOnPrimary">@color/white</item>     </style> 
 
</resources> 
 Apply Theme in AndroidManifest.xml 
<application 
    android:theme="@style/Theme.ResourceDemo"> 
 
5.	Drawable Resource (Shape)  res/drawable/rounded_bg.xml 
<shape xmlns:android="http://schemas.android.com/apk/res/android"> 
    <solid android:color="@color/teal_200" /> 
    <corners android:radius="12dp" /> 
    <padding         android:left="10dp"         android:right="10dp"         android:top="10dp"         android:bottom="10dp"/> 
</shape> 
 
6.	Image Resource 
Add any image (e.g., sample_image.png)  res/drawable/sample_image.png 
 
7.	activity_main.xml   res/layout/activity_main.xml 
LG College of Commerce and Economics 	2 
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:layout_width="match_parent"     android:layout_height="match_parent"     android:orientation="vertical"     android:padding="@dimen/padding" 
    android:background="@color/white"> 
 
    <TextView 
        android:id="@+id/textView"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="@string/welcome_text"         android:textSize="@dimen/text_size" 
        android:textColor="@color/black" /> 
 
    <ImageView         android:layout_width="200dp"         android:layout_height="200dp"         android:src="@drawable/sample_image" 
        android:layout_marginTop="20dp" /> 
 
    <Button 
        android:id="@+id/button"         android:layout_width="match_parent"         android:layout_height="@dimen/button_height"         android:text="@string/click_me"         android:layout_marginTop="20dp"         android:background="@drawable/rounded_bg" 
        android:textColor="@color/black" /> 
 
</LinearLayout> 
  
8. MainActivity.kt (Kotlin Code)  MainActivity.kt 
package com.example.resourcedemo 
 
import android.os.Bundle import android.widget.Button import android.widget.Toast import androidx.appcompat.app.AppCompatActivity 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
 
        val button = findViewById<Button>(R.id.button) 
 
        button.setOnClickListener {             Toast.makeText( 
                this, 
                getString(R.string.welcome_text), 
                Toast.LENGTH_SHORT 
            ).show() 
        } 
    } 
} 
 
OUTPUT: 
 
 
 
 
 
 
 
 
Practical No: 02 
AIM : Programming Activities and fragments Activity Life Cycle, Activity methods, Multiple Activities, Life Cycle of fragments and multiple fragments 
Project Structure 
MyApplication 
│ 
├── java/com/example/myapplication 
│      ├── MainActivity.kt 
│      ├── SecondActivity.kt 
│      ├── FirstFragment.kt 
│      ├── SecondFragment.kt 
│ 
├── res/layout 
│      ├── activity_main.xml 
│      ├── activity_second.xml 
│      ├── fragment_first.xml 
│      ├── fragment_second.xml 
│ 
└── AndroidManifest.xml 
2. MainActivity.kt (Lifecycle + Fragment + Multiple Activity) 
package com.example.myapplication 
 
import android.content.Intent import androidx.appcompat.app.AppCompatActivity 
import android.os.Bundle import android.util.Log 
import android.widget.Button 
 
class MainActivity : AppCompatActivity() { 
 
override fun onCreate(savedInstanceState: Bundle?) { super.onCreate(savedInstanceState) 
setContentView(R.layout.activity_main) 
 
Log.d("Lifecycle","onCreate") 
 
// Load First Fragment supportFragmentManager.beginTransaction() 
.replace(R.id.fragmentContainer, FirstFragment()) 
.commit() 
 
val btn = findViewById<Button>(R.id.btnNext) 
 
btn.setOnClickListener { 
 
startActivity( 
Intent(this, SecondActivity::class.java) 
) 
 
} 
} 
 
override fun onStart() { super.onStart() 
Log.d("Lifecycle","onStart") 
} 
 
override fun onResume() { super.onResume() 
Log.d("Lifecycle","onResume") 
} 
 
override fun onPause() { super.onPause() 
Log.d("Lifecycle","onPause") 
} 
 
override fun onStop() { super.onStop() 
Log.d("Lifecycle","onStop") 
} 
 
override fun onDestroy() { super.onDestroy() 
Log.d("Lifecycle","onDestroy") 
} 
} 
  
3. activity_main.xml 
Put inside: 
 res → layout → activity_main.xml 
 
<?xml version="1.0" encoding="utf-8"?> 
 
<LinearLayout 
xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:gravity="center" android:layout_width="match_parent" 
android:layout_height="match_parent"> 
 
<Button 
android:id="@+id/btnNext" android:text="Open Second Activity" 
 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
android:layout_width="wrap_content" android:layout_height="wrap_content"/> 
 
<FrameLayout android:id="@+id/fragmentContainer" android:layout_width="match_parent" android:layout_height="300dp"/> 
 
</LinearLayout> 4. SecondActivity.kt 
package com.example.myapplication 
 
import androidx.appcompat.app.AppCompatActivity import android.os.Bundle 
 
class SecondActivity : AppCompatActivity() { 
 
override fun onCreate(savedInstanceState: Bundle?) { super.onCreate(savedInstanceState) setContentView(R.layout.activity_second) 
} 
} 
5. activity_second.xml 
<LinearLayout 
xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="center" android:layout_width="match_parent" android:layout_height="match_parent"> 
 
<TextView 
android:text="Second Activity" android:textSize="22sp" android:layout_width="wrap_content" android:layout_height="wrap_content"/> 
 
</LinearLayout> 6. FirstFragment.kt 
package com.example.myapplication 
 
import android.os.Bundle import android.view.* import android.widget.Button 
import androidx.fragment.app.Fragment 
 
class FirstFragment : Fragment() { 
 
override fun onCreateView( 
LG College of Commerce and Economics 	7 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle? 
): View? { 
 
val view = inflater.inflate( R.layout.fragment_first, container, 
false 
) 
 
val btn = view.findViewById<Button>(R.id.btnFragment) 
 
btn.setOnClickListener { 
 
parentFragmentManager.beginTransaction() 
.replace( 
R.id.fragmentContainer, 
SecondFragment() 
) 
.commit() 
 
} 
 
return view 
} 
} 
7. fragment_first.xml 
<LinearLayout 
xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="center" android:layout_width="match_parent" android:layout_height="match_parent"> 
 
<Button android:id="@+id/btnFragment" android:text="Open Second Fragment" android:layout_width="wrap_content" android:layout_height="wrap_content"/> 
 
</LinearLayout> 
8. SecondFragment.kt 
package com.example.myapplication 
 
import android.os.Bundle import android.view.* import androidx.fragment.app.Fragment 
 
LG College of Commerce and Economics 	8 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
class SecondFragment : Fragment() { 
 
override fun onCreateView( inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle? 
): View? { 
 
return inflater.inflate( 
R.layout.fragment_second, 
container, 
false 
) 
 
} 
} 
9. fragment_second.xml 
<LinearLayout 
xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="center" android:layout_width="match_parent" android:layout_height="match_parent"> 
 
<TextView 
android:text="Second Fragment" android:textSize="20sp" android:layout_width="wrap_content" android:layout_height="wrap_content"/> 
 
</LinearLayout> 
 
10. AndroidManifest.xml (Important) 
Inside <application> add: 
<activity android:name=".SecondActivity"/> 
 
<activity 
android:name=".MainActivity"> 
 
<intent-filter> 
 
<action android:name="android.intent.action.MAIN"/> 
 
<category android:name="android.intent.category.LAUNCHER"/> 
 
</intent-filter> 
 
</activity> 
LG College of Commerce and Economics 	9 
 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
Practical No : 03 
AIM : Programs related to different Layouts Coordinate, Linear, Relative, Table, Absolute, Frame, List View, Grid View. MainActivity.kt (Kotlin) 
package com.example.layoutsapp 
 
import android.os.Bundle import android.widget.ArrayAdapter import android.widget.GridView import android.widget.ListView 
import androidx.appcompat.app.AppCompatActivity 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        // ListView Data 
        val listView = findViewById<ListView>(R.id.listView)         val listItems = arrayOf("Android", "Java", "Kotlin", "XML")         val listAdapter = ArrayAdapter(             this, 
            android.R.layout.simple_list_item_1,             listItems 
        ) 
        listView.adapter = listAdapter  
        // GridView Data 
        val gridView = findViewById<GridView>(R.id.gridView)         val gridItems = arrayOf("One", "Two", "Three", "Four")         val gridAdapter = ArrayAdapter(             this, 
            android.R.layout.simple_list_item_1,             gridItems 
        ) 
        gridView.adapter = gridAdapter 
    } 
} 
activity_main.xml (ALL LAYOUTS TOGETHER) 
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"     xmlns:app="http://schemas.android.com/apk/res-auto"     android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
    <LinearLayout 
        android:orientation="vertical"         android:padding="16dp"         android:layout_width="match_parent"         android:layout_height="wrap_content"> 
 
        <!-- 1. Linear Layout --> 
11 
LG College of Commerce and Economics 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        <TextView 
            android:text="Linear Layout"             android:textSize="18sp"             android:textStyle="bold"          android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <LinearLayout 
            android:orientation="horizontal"             android:layout_width="match_parent"             android:layout_height="wrap_content"> 
 
            <Button 
                android:text="Button 1"                 android:layout_width="0dp"                 android:layout_weight="1"                 android:layout_height="wrap_content"/> 
 
            <Button 
                android:text="Button 2"                 android:layout_width="0dp"                 android:layout_weight="1"                 android:layout_height="wrap_content"/>         </LinearLayout> 
 
        <!-- 2. Relative Layout --> 
        <TextView 
            android:text="Relative Layout"             android:textSize="18sp"             android:textStyle="bold"            android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <RelativeLayout 
            android:layout_width="match_parent"             android:layout_height="100dp"> 
 
            <TextView 
                android:id="@+id/relText"                 android:text="Hello Relative"                 android:layout_centerHorizontal="true"                 android:layout_width="wrap_content"                 android:layout_height="wrap_content"/> 
 
            <Button 
                android:text="Click" 
                android:layout_below="@id/relText"                 android:layout_centerHorizontal="true"                 android:layout_width="wrap_content"                 android:layout_height="wrap_content"/>         </RelativeLayout> 
 
        <!-- 3. Absolute Layout (Deprecated) --> 
        <TextView 
            android:text="Absolute Layout"             android:textSize="18sp"             android:textStyle="bold"            android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
LG College of Commerce and Economics 	12 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
        <AbsoluteLayout 
            android:layout_width="match_parent"             android:layout_height="120dp"> 
 
            <Button 
                android:text="ABS"                 android:layout_x="80dp"                 android:layout_y="40dp"                 android:layout_width="wrap_content"                 android:layout_height="wrap_content"/> 
        </AbsoluteLayout> 
 
        <!-- 4. Frame Layout --> 
        <TextView 
            android:text="Frame Layout"             android:textSize="18sp"             android:textStyle="bold"          android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <FrameLayout 
            android:layout_width="match_parent"             android:layout_height="100dp"> 
 
            <TextView 
                android:text="Centered Frame"                 android:layout_gravity="center"                 android:layout_width="wrap_content"                 android:layout_height="wrap_content"/> 
        </FrameLayout> 
 
        <!-- 5. Table Layout --> 
        <TextView 
            android:text="Table Layout"             android:textSize="18sp"             android:textStyle="bold"         android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <TableLayout 
            android:layout_width="match_parent"             android:layout_height="wrap_content"> 
 
            <TableRow> 
                <TextView android:text="Name"/> 
                <EditText android:layout_width="150dp"/>             </TableRow>  
            <TableRow> 
                <TextView android:text="Age"/> 
                <EditText android:layout_width="150dp"/> 
            </TableRow> 
        </TableLayout> 
 
        <!-- 6. Constraint (Coordinate) Layout --> 
        <TextView             android:text="Constraint Layout" 
LG College of Commerce and Economics 	13 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
            android:textSize="18sp"             android:textStyle="bold"          android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <androidx.constraintlayout.widget.ConstraintLayout             android:layout_width="match_parent"             android:layout_height="120dp"> 
 
            <Button 
                android:text="Center" 
                app:layout_constraintTop_toTopOf="parent"                 app:layout_constraintBottom_toBottomOf="parent"                 app:layout_constraintStart_toStartOf="parent"                 app:layout_constraintEnd_toEndOf="parent"                 android:layout_width="wrap_content"                 android:layout_height="wrap_content"/> 
        </androidx.constraintlayout.widget.ConstraintLayout> 
 
        <!-- 7. ListView --> 
        <TextView 
            android:text="ListView"             android:textSize="18sp"             android:textStyle="bold"         android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <ListView 
            android:id="@+id/listView"             android:layout_width="match_parent"             android:layout_height="150dp"/> 
 
        <!-- 8. GridView --> 
        <TextView 
            android:text="GridView"             android:textSize="18sp"             android:textStyle="bold"         android:layout_width="match_parent"         android:layout_height="wrap_content"/> 
 
        <GridView 
            android:id="@+id/gridView"             android:numColumns="2"             android:layout_width="match_parent"             android:layout_height="150dp"/> 
 
    </LinearLayout> 
</ScrollView> 
 
 
 
 
 
 
LG College of Commerce and Economics 	14 
 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
Practical No : 04 
AIM : Programming UI  Elements AppBar ,Fragments,UI Components  
1. Project Structure com.example.uiexample 
│── MainActivity.kt 
│── fragments 
│    ├── HomeFragment.kt 
│    └── ProfileFragment.kt 
│── res 
│    ├── layout 
│    │    ├── activity_main.xml 
│    │    ├── fragment_home.xml 
│    │    └── fragment_profile.xml 
│    └── menu 
│         └── app_menu.xml 
 
2. activity_main.xml (AppBar + Fragment Container) 
<?xml version="1.0" encoding="utf-8"?> 
<androidx.coordinatorlayout.widget.CoordinatorLayout     xmlns:android="http://schemas.android.com/apk/res/android"     xmlns:app="http://schemas.android.com/apk/res-auto"     android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
    <com.google.android.material.appbar.AppBarLayout         android:layout_width="match_parent"         android:layout_height="wrap_content"> 
 
LG College of Commerce and Economics 	16 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        <androidx.appcompat.widget.Toolbar             android:id="@+id/toolbar"             android:layout_width="match_parent"             android:layout_height="wrap_content"             android:background="?attr/colorPrimary"             app:title="UI Demo"             app:titleTextColor="@android:color/white" /> 
    </com.google.android.material.appbar.AppBarLayout> 
 
    <FrameLayout         android:id="@+id/fragment_container"         android:layout_width="match_parent"         android:layout_height="match_parent"         app:layout_behavior="@string/appbar_scrolling_view_behavior" /> 
 
</androidx.coordinatorlayout.widget.CoordinatorLayout> 
 
3. MainActivity.kt package com.example.uiexample 
 
import android.os.Bundle import androidx.appcompat.app.AppCompatActivity import androidx.appcompat.widget.Toolbar import com.example.uiexample.fragments.HomeFragment 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        val toolbar: Toolbar = findViewById(R.id.toolbar) 
LG College of Commerce and Economics 	17 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        setSupportActionBar(toolbar) 
 
        if (savedInstanceState == null) {             supportFragmentManager.beginTransaction() 
                .replace(R.id.fragment_container, HomeFragment()) 
                .commit() 
        } 
    } 
} 
 
4. fragment_home.xml (UI Components) <?xml version="1.0" encoding="utf-8"?> 
<LinearLayout     xmlns:android="http://schemas.android.com/apk/res/android"     android:orientation="vertical"     android:padding="16dp"     android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
    <TextView         android:id="@+id/txtTitle"         android:text="Home Fragment"         android:textSize="22sp"         android:textStyle="bold"         android:layout_width="wrap_content"         android:layout_height="wrap_content" /> 
 
    <EditText         android:id="@+id/edtName"         android:hint="Enter your name" 
LG College of Commerce and Economics 	18 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        android:layout_width="match_parent"         android:layout_height="wrap_content" /> 
 
    <Button         android:id="@+id/btnSubmit"         android:text="Submit"         android:layout_width="wrap_content"         android:layout_height="wrap_content" /> 
 
    <CheckBox         android:id="@+id/chkAgree"         android:text="I Agree"         android:layout_width="wrap_content"         android:layout_height="wrap_content" /> 
 
</LinearLayout> 
 
 
5. HomeFragment.kt package com.example.uiexample.fragments 
 
import android.os.Bundle import android.view.LayoutInflater import android.view.View import android.view.ViewGroup import android.widget.Button import android.widget.EditText import android.widget.Toast import androidx.fragment.app.Fragment import com.example.uiexample.R 
 
class HomeFragment : Fragment() { 
LG College of Commerce and Economics 	19 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
    override fun onCreateView(         inflater: LayoutInflater, container: ViewGroup?,         savedInstanceState: Bundle? 
    ): View? {         val view = inflater.inflate(R.layout.fragment_home, container, false) 
 
        val edtName = view.findViewById<EditText>(R.id.edtName)         val btnSubmit = view.findViewById<Button>(R.id.btnSubmit) 
 
        btnSubmit.setOnClickListener {             Toast.makeText( 
                activity, 
                "Hello ${edtName.text}", 
                Toast.LENGTH_SHORT 
            ).show() 
        }         return view 
    } 
} 
 
 
6. fragment_profile.xml (Second Fragment Example) 
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout     xmlns:android="http://schemas.android.com/apk/res/android"     android:orientation="vertical"     android:gravity="center"     android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
LG College of Commerce and Economics 	20 
T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
    <TextView         android:text="Profile Fragment"         android:textSize="20sp"         android:layout_width="wrap_content"         android:layout_height="wrap_content" /> 
</LinearLayout> 
OUTPUT: 
  
 
 
 
21 
LG College of Commerce and Economics 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
Practical No : 05 
AIM : Programming menu ,dialog and dialog fragments 
Project Structure 
com.example.menudialogdemo 
│── MainActivity.kt 
│── dialogs 
│    |─ MyDialogFragment.kt 
│── res 
│    |── layout 
│    │    |── activity_main.xml 
│    |── menu 
│         |── main_menu.xml 
 
activity_main.xml 
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:orientation="vertical"     android:gravity="center"     android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
    <Button         android:id="@+id/btnDialog"         android:text="Show Alert Dialog"         android:layout_width="wrap_content"         android:layout_height="wrap_content" /> 
 
    <Button 
        android:id="@+id/btnDialogFragment"         android:text="Show Dialog Fragment"         android:layout_width="wrap_content"         android:layout_height="wrap_content" /> 
</LinearLayout> 
 
Menu XML (res/menu/main_menu.xml) 
<?xml version="1.0" encoding="utf-8"?> 
<menu xmlns:android="http://schemas.android.com/apk/res/android"> 
 
    <item 
        android:id="@+id/menu_settings"         android:title="Settings" /> 
 
    <item 
LG College of Commerce and Economics 	22 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        android:id="@+id/menu_about"         android:title="About" /> 
</menu> 
 
MainActivity.kt (Menu + Dialog) package com.example.menudialogdemo 
 
import android.os.Bundle import android.view.Menu import android.view.MenuItem import android.widget.Button import android.widget.Toast import androidx.appcompat.app.AlertDialog import androidx.appcompat.app.AppCompatActivity import com.example.menudialogdemo.dialogs.MyDialogFragment 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        findViewById<Button>(R.id.btnDialog).setOnClickListener {             showAlertDialog() 
        } 
 
        findViewById<Button>(R.id.btnDialogFragment).setOnClickListener { 
            MyDialogFragment().show(supportFragmentManager, "MyDialog") 
        } 
    } 
 
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {         menuInflater.inflate(R.menu.main_menu, menu)         return true 
    } 
 
    override fun onOptionsItemSelected(item: MenuItem): Boolean {         return when (item.itemId) { 
            R.id.menu_settings -> { 
                Toast.makeText(this, "Settings clicked", Toast.LENGTH_SHORT).show()                 true 
            } 
            R.id.menu_about -> { 
                Toast.makeText(this, "About clicked", Toast.LENGTH_SHORT).show()                 true             } 
LG College of Commerce and Economics 	23 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
            else -> super.onOptionsItemSelected(item) 
        } 
    } 
 
    private fun showAlertDialog() {         AlertDialog.Builder(this) 
            .setTitle("Alert Dialog") 
            .setMessage("Do you want to continue?") 
            .setPositiveButton("Yes") { _, _ -> 
                Toast.makeText(this, "Yes clicked", Toast.LENGTH_SHORT).show() 
            } 
            .setNegativeButton("No") { _, _ -> 
                Toast.makeText(this, "No clicked", Toast.LENGTH_SHORT).show() 
            } 
            .show() 
    } 
} 
 
DialogFragment Example (MyDialogFragment.kt) package com.example.menudialogdemo.dialogs 
 
import android.app.Dialog import android.os.Bundle import androidx.appcompat.app.AlertDialog import androidx.fragment.app.DialogFragment 
 
class MyDialogFragment : DialogFragment() { 
 
    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {         return AlertDialog.Builder(requireContext()) 
            .setTitle("Dialog Fragment") 
            .setMessage("This is a Dialog Fragment") 
            .setPositiveButton("OK") { _, _ -> } 
            .setNegativeButton("Cancel") { _, _ -> } 
            .create() 
    } 
} 
 
 
 
 
 
 
 
LG College of Commerce and Economics 	24 
 
OUTPUT: 

 
 
 
Practical No :06 
Programs on Intents, Events, Listeners and Adapters The Android Intent Class, Using Events and Event Listeners 
1. Programming Using Android Intent Class (Kotlin) 
Intent is used to move from one Activity to another or send data between activities. 
Project Structure 
IntentDemoApp 
│ 
├── java/com.example.intentdemo 
│       ├── MainActivity.kt 
│       └── SecondActivity.kt 
│ 
├── res 
│   ├── layout 
│   │      ├── activity_main.xml 
│   │      └── activity_second.xml 
│ 
└── AndroidManifest.xml 
Step 1 — activity_main.xml 
<?xml version="1.0" encoding="utf-8"?> 
 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  android:layout_width="match_parent"  android:layout_height="match_parent"  android:gravity="center" 
 android:orientation="vertical"> 
 
<Button 
 android:id="@+id/btnNext"  android:text="Go To Second Activity"  android:layout_width="wrap_content" 
 android:layout_height="wrap_content"/> 
 
</LinearLayout> 
Step 2 — activity_second.xml 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  android:layout_width="match_parent"  android:layout_height="match_parent"  android:gravity="center"> 
 
<TextView  android:id="@+id/tvMsg"  android:textSize="22sp"  android:text="Welcome"  android:layout_width="wrap_content" 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 android:layout_height="wrap_content"/> 
 
</LinearLayout> 
Step 3 — MainActivity.kt 
package com.example.intentdemo 
 
import android.content.Intent import androidx.appcompat.app.AppCompatActivity import android.os.Bundle 
import android.widget.Button 
 
class MainActivity : AppCompatActivity() { 
 
 override fun onCreate(savedInstanceState: Bundle?) {   super.onCreate(savedInstanceState)   setContentView(R.layout.activity_main) 
 
  val btn = findViewById<Button>(R.id.btnNext) 
 
  btn.setOnClickListener { 
 
   val intent = Intent(this, SecondActivity::class.java) 
 
   intent.putExtra("message","Hello From Main Activity") 
 
   startActivity(intent) 
  } 
 } } 
Step 4 — SecondActivity.kt 
package com.example.intentdemo 
 
import androidx.appcompat.app.AppCompatActivity import android.os.Bundle import android.widget.TextView 
 
class SecondActivity : AppCompatActivity() { 
 
 override fun onCreate(savedInstanceState: Bundle?) {   super.onCreate(savedInstanceState)   setContentView(R.layout.activity_second) 
 
  val tv = findViewById<TextView>(R.id.tvMsg) 
 
  val msg = intent.getStringExtra("message") 
 
  tv.text = msg 
LG College of Commerce and Economics 	28 
 } } 
Step 5 — AndroidManifest.xml 
(Add Second Activity inside <application>) <activity android:name=".SecondActivity"/> 
OUTPUT: 
                   
2. Using Events and Event Listeners in Kotlin 
Event Listener responds when user clicks button or interacts with UI. 
Project Structure 
EventListenerApp 
│ 
├── MainActivity.kt 
│ 
├── layout 
│      └── activity_main.xml 
│ 
└── AndroidManifest.xml 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
activity_main.xml 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  android:layout_width="match_parent"  android:layout_height="match_parent"  android:gravity="center"  android:orientation="vertical"> 
 
<Button  android:id="@+id/btnClick"  android:text="Click Me"  android:layout_width="wrap_content"  android:layout_height="wrap_content"/> 
 
<TextView 
 android:id="@+id/tvResult"  android:textSize="22sp"  android:layout_width="wrap_content"  android:layout_height="wrap_content"/> 
 
</LinearLayout> MainActivity.kt 
package com.example.eventlistener 
 
import androidx.appcompat.app.AppCompatActivity import android.os.Bundle import android.widget.Button 
import android.widget.TextView 
 
class MainActivity : AppCompatActivity() { 
 
 override fun onCreate(savedInstanceState: Bundle?) {   super.onCreate(savedInstanceState)   setContentView(R.layout.activity_main) 
 
  val btn = findViewById<Button>(R.id.btnClick)   val tv = findViewById<TextView>(R.id.tvResult) 
 
  btn.setOnClickListener { 
 
   tv.text = "Button Clicked Successfully" 
 
  } 
 } } 
 
 
 
LG College of Commerce and Economics 	30 
OUTPUT: 
  
 
 
3. Programming Using Adapter (ListView Adapter) 
 Adapter connects data with UI components like ListView or RecyclerView. 
Project Structure 
AdapterDemoApp 
│ 
├── MainActivity.kt 
│ 
├── layout 
│      └── activity_main.xml 
│ 
└── AndroidManifest.xml 
 
 activity_main.xml 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  android:layout_width="match_parent" 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 android:layout_height="match_parent"> 
   
<ListView 
 android:id="@+id/listView"  android:layout_width="match_parent"  android:layout_height="match_parent"/> 
 
</LinearLayout> 
 
 MainActivity.kt 
package com.example.adapterdemo 
 
import androidx.appcompat.app.AppCompatActivity import android.os.Bundle import android.widget.ArrayAdapter import android.widget.ListView 
import android.widget.Toast 
 
class MainActivity : AppCompatActivity() { 
 
 override fun onCreate(savedInstanceState: Bundle?) { 
 
  super.onCreate(savedInstanceState)   setContentView(R.layout.activity_main) 
 
  val listView = findViewById<ListView>(R.id.listView) 
 
  val students = arrayOf( 
   "Vishal", 
   "Rahul", 
   "Sneha", 
   "Amit", 
   "Neha" 
  ) 
 
  val adapter = ArrayAdapter(    this, 
   android.R.layout.simple_list_item_1,    students 
  ) 
 
  listView.adapter = adapter 
 
  listView.setOnItemClickListener { _, _, position, _ -> 
 
   Toast.makeText( 
    this, 
    "Selected : ${students[position]}", 
LG College of Commerce and Economics 	32 
    Toast.LENGTH_SHORT 
   ).show() 
  } 
 } } 
OUTPUT: 
  
  
 
Practical No: 07 
AIM: Programs on Services, notification and broadcast receivers. 
  
 
MainActivity.kt 
package com.example.myapplication 
 
import android.Manifest import android.app.NotificationChannel import android.app.NotificationManager import android.content.BroadcastReceiver import android.content.Context import android.content.Intent import android.content.IntentFilter import android.content.pm.PackageManager 
import android.os.Build import android.os.Bundle import android.widget.Button import android.widget.Toast import androidx.appcompat.app.AppCompatActivity import androidx.core.app.ActivityCompat import androidx.core.app.NotificationCompat import androidx.core.app.NotificationManagerCompat import androidx.core.content.ContextCompat 
 
class MainActivity : AppCompatActivity() { 
 
    private val channelId = "MyChannel"     private val notificationPermissionCode = 1001 
 
    // 🔹 Dynamic Broadcast Receiver 
    private val myReceiver = object : BroadcastReceiver() {         override fun onReceive(context: Context, intent: Intent) { 
            if (intent.action == "com.example.myapplication.CUSTOM_BROADCAST") { 
                Toast.makeText(context, "Broadcast Received!", Toast.LENGTH_SHORT).show() 
            } 
        } 
    } 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState) 
        setContentView(R.layout.activity_main) 
 
        val startServiceBtn = findViewById<Button>(R.id.startServiceBtn)         val stopServiceBtn = findViewById<Button>(R.id.stopServiceBtn)         val showNotificationBtn = findViewById<Button>(R.id.showNotificationBtn)         val sendBroadcastBtn = findViewById<Button>(R.id.sendBroadcastBtn) 
 
        // 🔹 Register Broadcast Receiver (Android 13+ safe) 
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {             registerReceiver(                 myReceiver, 
                IntentFilter("com.example.myapplication.CUSTOM_BROADCAST"), 
                RECEIVER_NOT_EXPORTED 
            ) 
        } 
 
        createNotificationChannel() 
 
        // 🔹 Show Notification Button         showNotificationBtn.setOnClickListener {             if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {                 if (ContextCompat.checkSelfPermission(                         this, 
                        Manifest.permission.POST_NOTIFICATIONS 
                    ) == PackageManager.PERMISSION_GRANTED 
                ) { 
                    showNotification() 
                } else { 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
                    ActivityCompat.requestPermissions(                         this, 
                        arrayOf(Manifest.permission.POST_NOTIFICATIONS),                         notificationPermissionCode 
                    ) 
                } 
            } else { 
                showNotification() 
            } 
        } 
 
        // 🔹 Start Service Button 
        startServiceBtn.setOnClickListener {             startService(Intent(this, MyService::class.java)) 
            Toast.makeText(this, "Start Service Button Clicked", 
Toast.LENGTH_SHORT).show() 
        } 
 
        // 🔹 Stop Service Button 
        stopServiceBtn.setOnClickListener {             stopService(Intent(this, MyService::class.java)) 
            Toast.makeText(this, "Stop Service Button Clicked", 
Toast.LENGTH_SHORT).show() 
        } 
 
        // 🔹 Send Broadcast Button 
        sendBroadcastBtn.setOnClickListener {             val intent = Intent("com.example.myapplication.CUSTOM_BROADCAST")             intent.setPackage(packageName)   // Important for non-exported receiver             sendBroadcast(intent) 
            Toast.makeText(this, "Broadcast Sent", Toast.LENGTH_SHORT).show() 
        } 
    } 
 
    // 🔹 Create Notification Channel     private fun createNotificationChannel() {         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {             val name = "My Channel" 
            val descriptionText = "My Channel Description"             val importance = NotificationManager.IMPORTANCE_DEFAULT 
 
            val channel = NotificationChannel(channelId, name, importance).apply {                 description = descriptionText 
            } 
 
            val notificationManager =                 getSystemService(NotificationManager::class.java) 
 
            notificationManager.createNotificationChannel(channel) 
LG College of Commerce and Economics 	36 
 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        } 
    } 
 
    // 🔹 Show Notification     private fun showNotification() {         val notification = NotificationCompat.Builder(this, channelId) 
            .setSmallIcon(R.drawable.ic_launcher_foreground) 
            .setContentTitle("Hello Notification") 
            .setContentText("This is a simple notification in Kotlin") 
            .setPriority(NotificationCompat.PRIORITY_DEFAULT) 
            .build() 
 
        try { 
            NotificationManagerCompat.from(this).notify(1, notification)         } catch (e: SecurityException) {             e.printStackTrace() 
        } 
    } 
 
    // 🔹 Handle Notification Permission Result     override fun onRequestPermissionsResult(         requestCode: Int,         permissions: Array<out String>,         grantResults: IntArray 
    ) { 
        super.onRequestPermissionsResult(requestCode, permissions, grantResults) 
 
        if (requestCode == notificationPermissionCode &&             grantResults.isNotEmpty() &&             grantResults[0] == PackageManager.PERMISSION_GRANTED 
        ) { 
            showNotification() 
        } 
    } 
 
    // 🔹 Unregister Receiver     override fun onDestroy() {         super.onDestroy()         unregisterReceiver(myReceiver) 
    } 
} 
 
MyReceiver.kt 
 
package com.example.myapplication 
 
import android.content.BroadcastReceiver import android.content.Context import android.content.Intent import android.widget.Toast 
LG College of Commerce and Economics 	37 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
class MyReceiver : BroadcastReceiver() { 
 
    override fun onReceive(context: Context, intent: Intent) { 
        if (intent.action == "com.example.myapplication.CUSTOM_BROADCAST") { 
            Toast.makeText(context, "Broadcast Received!", Toast.LENGTH_SHORT).show() 
        } 
    } 
} 
 
 
activity_main.xml 
 
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:layout_width="match_parent"     android:layout_height="match_parent" 
    android:orientation="vertical"     android:padding="24dp"     android:gravity="center" 
    android:background="#FFFFFF"> 
 
    <TextView 
        android:id="@+id/titleText"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Services, Notification  Broadcast"         android:textSize="20sp"         android:textStyle="bold"         android:layout_marginBottom="24dp" /> 
 
    <Button         android:id="@+id/startServiceBtn"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="Start Service"         android:layout_marginBottom="12dp" /> 
 
    <Button         android:id="@+id/stopServiceBtn"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="Stop Service"         android:layout_marginBottom="12dp" /> 
 
    <Button         android:id="@+id/showNotificationBtn"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="Show Notification" 
38 
LG College of Commerce and Economics 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        android:layout_marginBottom="12dp" /> 
 
    <Button         android:id="@+id/sendBroadcastBtn"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="Send Broadcast" 
        android:layout_marginBottom="12dp" /> 
 
</LinearLayout> 
 
AndroidManifest.xml 
 
<?xml version="1.0" encoding="utf-8"?> 
<manifest xmlns:android="http://schemas.android.com/apk/res/android"     xmlns:tools="http://schemas.android.com/tools"> 
 
    <!-- Notification permission for Android 13+ --> 
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" /> 
 
    <application 
        android:allowBackup="true"         android:dataExtractionRules="@xml/data_extraction_rules"         android:fullBackupContent="@xml/backup_rules"         android:icon="@mipmap/ic_launcher"         android:label="@string/app_name"         android:roundIcon="@mipmap/ic_launcher_round"         android:supportsRtl="true"         android:theme="@style/Theme.MyApplication"> 
 
        <!-- Main Activity --> 
        <activity 
            android:name=".MainActivity"             android:exported="true"> 
            <intent-filter> 
                <action android:name="android.intent.action.MAIN" /> 
                <category android:name="android.intent.category.LAUNCHER" /> 
            </intent-filter> 
        </activity> 
 
        <!-- Service Registration --> 
        <service 
            android:name=".MyService"             android:exported="false" /> 
 
    </application> 
 
</manifest> 
 
 
39 
LG College of Commerce and Economics 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
MyService.kt 
package com.example.myapplication 
 
import android.app.Service import android.content.Intent import android.os.IBinder 
import android.widget.Toast 
 
class MyService : Service() { 
 
    override fun onCreate() {         super.onCreate() 
        Toast.makeText(this, "Service Created", Toast.LENGTH_SHORT).show() 
    } 
 
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {         Toast.makeText(this, "Service Started", Toast.LENGTH_SHORT).show()         return START_STICKY 
    } 
 
    override fun onDestroy() {         super.onDestroy() 
        Toast.makeText(this, "Service Stopped", Toast.LENGTH_SHORT).show() 
    } 
 
    override fun onBind(intent: Intent?): IBinder? {         return null 
    } 
} 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
LG College of Commerce and Economics 	40 
 
 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
Practical No : 08 (A) 
AIM :  Database Programming with SQLite 
Project Structure app/ 
└── src/main/ 
    ├── java/com/example/studentdatabase/ 
    │   ├── MainActivity.kt 
    │   └── DBHelper.kt 
    │ 
    ├── res/ 
    │   └── layout/ 
    │       └── activity_main.xml 
    │ 
    └── AndroidManifest.xml 
 
 DBHelper.kt (SQLite Database Code) package com.example.studentdatabase 
 
import android.content.ContentValues import android.content.Context import android.database.Cursor import android.database.sqlite.SQLiteDatabase import android.database.sqlite.SQLiteOpenHelper 
 
class DBHelper(context: Context) : 
    SQLiteOpenHelper(context, "StudentDB", null, 1) { 
 
    override fun onCreate(db: SQLiteDatabase) {         db.execSQL( 
            "CREATE TABLE student (" + 
                    "id INTEGER PRIMARY KEY AUTOINCREMENT," + 
                    "name TEXT," + 
                    "age INTEGER)" 
LG College of Commerce and Economics 	43 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        ) 
    } 
 
    override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {         db.execSQL("DROP TABLE IF EXISTS student") 
        onCreate(db) 
    } 
 
    fun insertStudent(name: String, age: Int): Boolean {         val db = writableDatabase         val values = ContentValues()         values.put("name", name)         values.put("age", age) 
 
        val result = db.insert("student", null, values)         return result != -1L 
    } 
 
    fun getStudents(): Cursor {         val db = readableDatabase         return db.rawQuery("SELECT * FROM student", null) 
    } 
 
    fun updateStudent(id: Int, name: String, age: Int): Boolean {         val db = writableDatabase         val values = ContentValues()         values.put("name", name)         values.put("age", age) 
 
        val result = db.update( 
            "student",             values,             "id=?",             arrayOf(id.toString()) 
LG College of Commerce and Economics 	44 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        ) 
        return result > 0 
    } 
 
    fun deleteStudent(id: Int): Boolean {         val db = writableDatabase         val result = db.delete( 
            "student",             "id=?",             arrayOf(id.toString()) 
        ) 
        return result > 0 
    } 
} 
MainActivity.kt  package com.example.studentdatabase 
 
import android.os.Bundle import android.widget.Button import android.widget.EditText import android.widget.TextView import androidx.appcompat.app.AppCompatActivity 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        val db = DBHelper(this) 
 
        val nameInput = findViewById<EditText>(R.id.nameInput)         val ageInput = findViewById<EditText>(R.id.ageInput)         val resultText = findViewById<TextView>(R.id.resultText) 
LG College of Commerce and Economics 	45 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
        findViewById<Button>(R.id.insertBtn).setOnClickListener {             val name = nameInput.text.toString()             val age = ageInput.text.toString().toInt()             db.insertStudent(name, age) 
        } 
 
        findViewById<Button>(R.id.viewBtn).setOnClickListener {             val cursor = db.getStudents()             val data = StringBuilder() 
 
            while (cursor.moveToNext()) {                 data.append( 
                    "ID: ${cursor.getInt(0)}  " + 
                    "Name: ${cursor.getString(1)}  " + 
                    "Age: ${cursor.getInt(2)}\n" 
                )             }             cursor.close()             resultText.text = data.toString() 
        } 
    } 
} 
 
 activity_main.xml  
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout     xmlns:android="http://schemas.android.com/apk/res/android"     android:layout_width="match_parent"     android:layout_height="match_parent"     android:orientation="vertical"     android:padding="16dp"> 
 
    <EditText 
LG College of Commerce and Economics 	46 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        android:id="@+id/nameInput"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:hint="Enter Name"/> 
 
    <EditText         android:id="@+id/ageInput"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:hint="Enter Age"         android:inputType="number"/> 
 
    <Button         android:id="@+id/insertBtn"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="Insert"/> 
 
    <Button         android:id="@+id/viewBtn"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="View"/> 
 
    <TextView         android:id="@+id/resultText"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:textSize="16sp"         android:paddingTop="10dp"/> 
</LinearLayout> 
 
AndroidManifest.xml 
<?xml version="1.0" encoding="utf-8"?> 
LG College of Commerce and Economics 	47 
 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
Practical No : 08(B) 
 
AIM : Programming Network Communications and Services (JSON) 
 
com.example.networkjsonapp 
│ 
├── MainActivity.kt 
│ 
├── model 
│     └── Student.kt 
│ 
├── network 
│     ├── ApiService.kt 
│     └── RetrofitClient.kt 
│ 
└── res 
      └── layout 
            └── activity_main.xml 
 
1. AndroidManifest.xml 
<manifest xmlns:android="http://schemas.android.com/apk/res/android"     package="com.example.networkjsonapp"> 
 
    <uses-permission android:name="android.permission.INTERNET"/> 
 
    <application 
        android:allowBackup="true"         android:label="NetworkJSONApp"         android:theme="@style/Theme.AppCompat.Light.NoActionBar"> 
 
        <activity android:name=".MainActivity"> 
            <intent-filter> 
                <action android:name="android.intent.action.MAIN"/> 
                <category android:name="android.intent.category.LAUNCHER"/> 
            </intent-filter> 
        </activity> 
 
    </application> 
</manifest> 
 
2.	Gradle Dependencies (build.gradle - Module) implementation 'com.squareup.retrofit2:retrofit:2.9.0' 
implementation 'com.squareup.retrofit2:converter-gson:2.9.0' 
 
3.	Model Class – Student.kt 
📁 model/Student.kt 
 
package com.example.networkjsonapp.model 
 
data class Student( 
LG College of Commerce and Economics 	49 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
    val id: Int,     val name: String,     val age: Int 
) 
4. API Interface – ApiService.kt 
📁 network/ApiService.kt 
 
package com.example.networkjsonapp.network 
 
import com.example.networkjsonapp.model.Student import retrofit2.Call 
import retrofit2.http.GET 
 
interface ApiService { 
 
    @GET("students.json") 
    fun getStudents(): Call<List<Student>> } 
Assume API URL: 
https://example.com/students.json 
 
5. Retrofit Client – RetrofitClient.kt 
📁 network/RetrofitClient.kt 
 
package com.example.networkjsonapp.network 
 
import retrofit2.Retrofit import retrofit2.converter.gson.GsonConverterFactory 
 
object RetrofitClient { 
 
    private const val BASE_URL = "https://example.com/" 
 
    val instance: ApiService by lazy {         val retrofit = Retrofit.Builder() 
            .baseUrl(BASE_URL) 
            .addConverterFactory(GsonConverterFactory.create()) 
            .build() 
 
        retrofit.create(ApiService::class.java) 
    } 
} 
 
6. UI Layout – activity_main.xml 
📁 res/layout/activity_main.xml 
 
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:orientation="vertical"     android:padding="16dp" 
LG College of Commerce and Economics 	50 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
    android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
    <Button 
        android:id="@+id/btnFetch"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:text="Fetch Students" /> 
 
    <TextView 
        android:id="@+id/txtResult"         android:layout_width="match_parent"         android:layout_height="wrap_content"         android:textSize="16sp"         android:paddingTop="16dp"/> 
</LinearLayout> 
 
7. Main Activity – MainActivity.kt 
package com.example.networkjsonapp 
 
import androidx.appcompat.app.AppCompatActivity import android.os.Bundle import android.widget.TextView 
import org.json.JSONArray 
 
class MainActivity : AppCompatActivity() { 
 
    lateinit var txtResult: TextView 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        txtResult = findViewById(R.id.txtResult) 
 
        loadJSONFromAssets() 
    } 
 
    private fun loadJSONFromAssets() {         val json = assets.open("students.json") 
            .bufferedReader() 
            .use { it.readText() } 
 
        val jsonArray = JSONArray(json)         val builder = StringBuilder() 
 
        for (i in 0 until jsonArray.length()) {             val obj = jsonArray.getJSONObject(i)             builder.append("ID: ${obj.getInt("id")}\n")             builder.append("Name: ${obj.getString("name")}\n") 
LG College of Commerce and Economics 	51 
T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
            builder.append("Age: ${obj.getInt("age")}\n\n") 
        } 
 
        txtResult.text = builder.toString() 
    } 
} 
 
 
8. Sample JSON from Server (students.json)  Place under –(app/src/main/assets/students.json) 
[ 
  { "id": 1, "name": "Vishal", "age": 21 }, 
  { "id": 2, "name": "Anita", "age": 19 }, 
  { "id": 3, "name": "Rahul", "age": 20 }, 
] 
OUTPUT: 
  
52 
LG College of Commerce and Economics 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
Practical No : 09 
AIM : Programming Threads, Handlers and Asynchronous Programs  
1. Programming Threads in Kotlin   Project Structure com.example.threadexample         └── MainActivity.kt res 
 └── layout 
        └── activity_main.xml 
 
activity_main.xml 
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:layout_width="match_parent"     android:layout_height="match_parent"     android:gravity="center"     android:orientation="vertical"> 
 
    <Button         android:id="@+id/btnThread"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Start Thread"/> 
 
    <TextView         android:id="@+id/tvResult"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Result"/> 
</LinearLayout> 
LG College of Commerce and Economics 	53 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
MainActivity.kt (Thread Example) package com.example.threadexample 
 
import android.os.Bundle import android.widget.Button import android.widget.TextView import androidx.appcompat.app.AppCompatActivity 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        val btnThread = findViewById<Button>(R.id.btnThread)         val tvResult = findViewById<TextView>(R.id.tvResult) 
 
        btnThread.setOnClickListener { 
 
            Thread { 
                Thread.sleep(3000) // Simulate long task 
 
                runOnUiThread {                     tvResult.text = "Thread Task Completed" 
                } 
            }.start() 
        } 
    } 
} 
LG College of Commerce and Economics 	54 
 
                   
 
 
 2. Handler Example 
MainActivity.kt (Handler Example) package com.example.threadexample 
  
import android.os.Bundle import android.widget.Button import android.widget.TextView import androidx.appcompat.app.AppCompatActivity import android.os.Handler import android.os.Looper  class MainActivity : AppCompatActivity() { 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
  
 	override fun onCreate(savedInstanceState: Bundle?) {      	super.onCreate(savedInstanceState)      	setContentView(R.layout.activity_main) 
  
     	val btnThread = findViewById<Button>(R.id.btnThread)      	val tvResult = findViewById<TextView>(R.id.tvResult)      	val handler = Handler(Looper.getMainLooper()) 
  
  
	     	btnThread.setOnClickListener { 
Thread { 
	 	Thread.sleep(3000) 
  
	 	handler.post { 
	     	tvResult.text = "Updated using Handler" 
	 	} 
  
	}.start()    	 
	     	} 
	 	} 
} 
 
 
 
 
 
 
 
 
LG College of Commerce and Economics 	56 
  
 3. Asynchronous Programming using Coroutines (Modern Method) 
 Add Dependency 
Add inside build.gradle (Module: app) implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3" 
 
MainActivity.kt (Coroutine Example) package com.example.threadexample 
 
import android.os.Bundle import android.widget.Button import android.widget.TextView import androidx.appcompat.app.AppCompatActivity 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
import kotlinx.coroutines.* 
 
class MainActivity : AppCompatActivity() { 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        val btnThread = findViewById<Button>(R.id.btnThread)         val tvResult = findViewById<TextView>(R.id.tvResult) 
 
        btnThread.setOnClickListener { 
 
            GlobalScope.launch(Dispatchers.IO) { 
 
                delay(3000) 
 
                withContext(Dispatchers.Main) {                     tvResult.text = "Coroutine Task Completed" 
                } 
            } 
        } 
    } 
} 
 
 
 
 
 
 
LG College of Commerce and Economics 	58 
                             
 
 
 
 
 
 
 
 
 
 
 
 
 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
Practical No:10(A) 
AIM:  Media + Telephone API Project   
📁 Project Structure  
MediaTelephoneApp/  
│  
├── app/  
│   ├── manifests/  
│   │     └── AndroidManifest.xml  
│   │  
│   ├── java/com/example/mediatelephoneapp/  
│   │     └── MainActivity.kt  
│   │  
│   ├── res/  
│   │   ├── layout/  
│   │   │     └── activity_main.xml  
│   │   │  
│   │   ├── raw/  
│   │   │     ├── song.mp3  
│   │   │     └── video.mp4  
│   │   │  
│   │   └── values/  
│   │         └── strings.xml  
│   │  
│   └── Gradle Scripts/  
│         └── build.gradle  
  
 AndroidManifest.xml  
<?xml version="1.0" encoding="utf-8"?> 
<manifest xmlns:android="http://schemas.android.com/apk/res/android"     package="com.example.mediatelephone"> 
 
    <!-- Permission --> 
    <uses-permission android:name="android.permission.CALL_PHONE"/> 
LG College of Commerce and Economics 	60 
 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
 
    <!-- Telephony feature (to remove warning) --> 
    <uses-feature         android:name="android.hardware.telephony"         android:required="false"/> 
 
    <application         android:allowBackup="true"         android:icon="@mipmap/ic_launcher"         android:roundIcon="@mipmap/ic_launcher_round"         android:theme="@style/Theme.AppCompat.Light.DarkActionBar"> 
 
        <activity             android:name=".MainActivity"             android:exported="true">  <!-- REQUIRED for Android 12+ --> 
 
            <intent-filter> 
                <action android:name="android.intent.action.MAIN"/> 
                <category android:name="android.intent.category.LAUNCHER"/> 
            </intent-filter> 
 
        </activity> 
 
    </application> </manifest> 
  
 activity_main.xml  
<?xml version="1.0" encoding="utf-8"?> 
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:layout_width="match_parent"     android:layout_height="match_parent"     android:orientation="vertical"     android:gravity="center"     android:padding="20dp"> 
 
    <Button         android:id="@+id/btnPlay"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Play Music"/> 
 
    <Button         android:id="@+id/btnPause"         android:layout_width="wrap_content"         android:layout_height="wrap_content" 
LG College of Commerce and Economics 	61 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        android:text="Pause"/> 
 
    <Button         android:id="@+id/btnStop"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Stop"/> 
 
    <VideoView         android:id="@+id/videoView"         android:layout_width="match_parent"         android:layout_height="200dp"/> 
 
    <Button         android:id="@+id/btnDial"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Open Dialer"/> 
 
    <Button         android:id="@+id/btnCall"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Direct Call"/> 
 
    <Button         android:id="@+id/btnSms"         android:layout_width="wrap_content"         android:layout_height="wrap_content"         android:text="Send SMS"/> 
 
</LinearLayout> 
  
  
MainActivity.kt  package com.example.mediatelephone 
 
import android.Manifest import android.content.Intent import android.content.pm.PackageManager import android.media.MediaPlayer import android.net.Uri import android.os.Bundle import android.widget.* 
import androidx.appcompat.app.AppCompatActivity 
LG College of Commerce and Economics 	62 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
import androidx.core.app.ActivityCompat 
 
class MainActivity : AppCompatActivity() { 
 
    private lateinit var player: MediaPlayer     private val CALL_PERMISSION = 101 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        val play = findViewById<Button>(R.id.btnPlay)         val pause = findViewById<Button>(R.id.btnPause)         val stop = findViewById<Button>(R.id.btnStop)         val dial = findViewById<Button>(R.id.btnDial)         val call = findViewById<Button>(R.id.btnCall)         val sms = findViewById<Button>(R.id.btnSms)         val videoView = findViewById<VideoView>(R.id.videoView) 
 
        // MEDIA PLAYER (Audio)         player = MediaPlayer.create(this, R.raw.song) 
 
        play.setOnClickListener { player.start() }         pause.setOnClickListener { player.pause() }         stop.setOnClickListener {             player.stop()             player.prepare() 
        } 
 
        // VIDEO PLAYER         val uri = Uri.parse("android.resource://$packageName/${R.raw.video}")         videoView.setVideoURI(uri)         videoView.start() 
 
        // OPEN DIALER         dial.setOnClickListener { 
            startActivity(Intent(Intent.ACTION_DIAL, Uri.parse("tel:9876543210"))) 
        } 
 
        // DIRECT CALL         call.setOnClickListener {             val intent = Intent(Intent.ACTION_CALL, Uri.parse("tel:9876543210")) 
 
            if (ActivityCompat.checkSelfPermission(this, Manifest.permission.CALL_PHONE) 
                != PackageManager.PERMISSION_GRANTED) { 
 
63 
LG College of Commerce and Economics 
T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
                ActivityCompat.requestPermissions(this,                     arrayOf(Manifest.permission.CALL_PHONE), CALL_PERMISSION) 
            } else {                 startActivity(intent) 
            } 
        } 
 
        // SMS         sms.setOnClickListener {             val intent = Intent(Intent.ACTION_SENDTO)             intent.data = Uri.parse("smsto:9876543210")             intent.putExtra("sms_body", "Hello from Android App")             startActivity(intent) 
        } 
    } 
} 
 
OUTPUT: 
 
  
  
 
 
 
64 
LG College of Commerce and Economics 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
	 	 	 	 	Practical No : 10(B) 
AIM: Security & Permissions Project (Camera Permission)  
📁 Project Structure  
SecurityPermissionApp/  
│  
├── app/  
│   ├── manifests/  
│   │     └── AndroidManifest.xml  
│   │  
│   ├── java/com/example/securitypermissionapp/  
│   │     └── MainActivity.kt  
│   │  
│   ├── res/  
│   │   ├── layout/  
│   │   │     └── activity_main.xml  
│   │   │  
│   │   └── values/  
│   │         └── strings.xml  
 AndroidManifest.xml  
<?xml version="1.0" encoding="utf-8"?> 
<manifest xmlns:android="http://schemas.android.com/apk/res/android"     package="com.example.security"> 
 
    <!-- Camera Permission --> 
    <uses-permission android:name="android.permission.CAMERA"/> 
 
    <!-- Optional but recommended --> 
    <uses-feature         android:name="android.hardware.camera"         android:required="true" /> 
 
    <application         android:allowBackup="true"         android:supportsRtl="true"         android:theme="@style/Theme.AppCompat.Light.DarkActionBar"> 
 
LG College of Commerce and Economics 	65 

T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
        <activity             android:name=".MainActivity"             android:exported="true">  <!-- IMPORTANT for Android 12+ --> 
 
            <intent-filter> 
                <action android:name="android.intent.action.MAIN"/> 
                <category android:name="android.intent.category.LAUNCHER"/> 
            </intent-filter> 
 
        </activity> 
 
    </application> 
 
</manifest>  
activity_main.xml  
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"     android:gravity="center"     android:orientation="vertical"     android:layout_width="match_parent"     android:layout_height="match_parent"> 
 
    <Button         android:id="@+id/btnCamera"         android:text="Open Camera"         android:layout_width="match_parent"         android:layout_height="match_parent"/> </LinearLayout> 
  
 MainActivity.kt  package com.example.security 
 
import android.Manifest import android.content.Intent import android.content.pm.PackageManager import android.os.Bundle import android.provider.MediaStore import android.widget.Button import android.widget.Toast import androidx.appcompat.app.AppCompatActivity import androidx.core.app.ActivityCompat 
 
class MainActivity : AppCompatActivity() { 
 
LG College of Commerce and Economics 	66 

	T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
    // ✅ Kotlin naming convention (camelCase)     private val cameraPermission = 200 
 
    override fun onCreate(savedInstanceState: Bundle?) {         super.onCreate(savedInstanceState)         setContentView(R.layout.activity_main) 
 
        val cameraBtn = findViewById<Button>(R.id.btnCamera) 
 
        cameraBtn.setOnClickListener {             checkPermission() 
        } 
    } 
 
    private fun checkPermission() {         if (ActivityCompat.checkSelfPermission(                 this, 
                Manifest.permission.CAMERA 
            ) != PackageManager.PERMISSION_GRANTED 
        ) { 
 
            ActivityCompat.requestPermissions(                 this, 
                arrayOf(Manifest.permission.CAMERA),                 cameraPermission 
            ) 
 
        } else { 
            openCamera() 
        } 
    } 
 
    private fun openCamera() {         val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)         startActivity(intent) 
    } 
 
    // ✅ IMPORTANT FIX: call super method     override fun onRequestPermissionsResult(         requestCode: Int,         permissions: Array<out String>,         grantResults: IntArray 
    ) { 
        super.onRequestPermissionsResult(requestCode, permissions, grantResults) 
 
        if (requestCode == cameraPermission && LG College of Commerce and Economics 	67 
T.Y.B.Sc.IT  	I.T Infrastructure Management  	36052 
            grantResults.isNotEmpty() &&             grantResults[0] == PackageManager.PERMISSION_GRANTED 
        ) { 
            openCamera() 
        } else { 
            Toast.makeText(this, "Permission Denied", Toast.LENGTH_SHORT).show() 
        } 
    } } 
OUTPUT: 
                             
 	                               
          
 
68 
LG College of Commerce and Economics 
